from typing import List

import pandas as pd
import requests
from googletrans import Translator

from .languages import LANGCODES


def make_translation(word: str) -> str:
    """
    Translate a word using GoogleTrans library
    The language might be indicate in the 2 first character
    :param word: string
    :param language: string
    :return: word string
    """
    if word == 'en:spreads':
        # better translation for the word spreads
        return 'Pate à tartiner'
    elif word == 'en:sweets-spreads':
        return 'Pâte à tartiner sucrée'
    elif word == 'en:plant-based-spreads':
        return 'Pâte à tartiner végétal'
    else:
        try:
            translator = Translator()
            # take the language indication
            language = get_language(word)
            # remove language indicator
            word = slice_language(word)
            # translate word to french
            word = translator.translate(word, src=language, dest='fr').text
            # remove any type of punctuation
            return word.replace('-', ' ')
        except ValueError:
            # if invalid language source return word
            return word.replace('-', ' ')


def detect_lang(word: str) -> str:
    """Detect language with googletrans"""
    translator = Translator()
    # detect language
    tr = translator.detect(word)
    for l in LANGCODES.values():
        if tr.lang == l:
            return tr.lang
    return 'unkonwn'


def slice_language(word: str) -> str:
    if len(word) > 3 and word[2] == ':':
        word = word[3:]
    return word


def get_language(word: str) -> str:
    """
    Return the language of the word if its has a language indicator.
    If its has not googletrans library will detect its language
    """
    if len(slice_language(word)) == len(word):
        # the word has no language indicator
        lang = detect_lang(word)
    else:
        lang = word[:2]
        translator = Translator()
        tr = translator.detect(word)
        # if language detected is different
        # the confidence of the translator is above 90 %
        # take the language from the translator
        if tr.confidence > 0.9 and tr.lang != lang:
            lang = tr.lang
    return lang


def normalize_value(value: float, unit: str) -> float:
    """Convert all value to mg, mL or kcal."""
    try:
        value = float(value)
    # if value can't be cast the value must be incorrect
    # return 0
        if unit.lower() == 'mg' or unit.lower() == 'kcal'or unit.lower() == 'ml':
            return value
        elif unit.lower() == 'kg':
            value = value * 1000000
        elif unit.lower() == 'g':
            value = value * 1000
        elif unit.lower() == 'µg':
            value = value / 1000
        elif unit.lower() == 'kj':
            value = value * 239.005
        elif unit.lower() == 'L':
            value = value * 1000
        elif unit == 'µL':
            value = value / 1000
        else:
            value = 0.0
        return value
    except ValueError:
        return 0.0
    except TypeError:
        return 0.0

class Singleton(type):
    """ Create a singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ProductDataFrame(metaclass=Singleton):
    """
    Generate a dataframe concatenating all pages founds related to
    the category on openfoodfacts.
    """

    def __init__(self, category: str):
        self.category = category

    def _count_pages(self, category: str) -> int:
        """
        Count pages for a category
        :return: page_number, integer
        """
        url = 'https://fr.openfoodfacts.org/categorie/'
        url += self.category + '.json'
        json_file = requests.get(url).json()
        page_number = json_file['count'] // 20
        if json_file['count'] % 20 != 0:
            page_number += 1
        return page_number

    def _generate_products(self, page: int) -> List:
        """
        Query the api by category and by page
        :param page: integer that fetch the api at the page number
        :return products['products']: json data containing all informations
        """
        url = 'https://fr.openfoodfacts.org/categorie/'
        url += self.category + '/' + str(page) + '.json'
        products = requests.get(url).json()
        return products['products']

    def _generate_dataframe(self):
        """
        Query openfoodfacts and concatenate the dataframe
        for every page in the category. The dataframe select
        column and remove empty row if some values are missing
        in the column.
        """
        nb_pages = self._count_pages(self.category) + 1
        for page in range(1, nb_pages):
            print(page)
            products = self._generate_products(page)
            df = pd.DataFrame(products)
            # Select columns
            try:
                df = df[[
                    'product_name',
                    'code',  # barcode
                    'image_small_url',  # url of the image of the product
                    'url',  # openfoodfacts url
                    'nutrition_grades',
                    'quantity',  # provide the measurement unit
                    'categories_hierarchy',   # list all categories
                    'additives_tags',  # list all additives
                    'allergens_hierarchy',  # list all allergens
                    'ingredients',  # list all ingredients
                    'nutriments',  # list all nutriments
                    'traces_hierarchy',  # list all traces of allergens
                ]]
                # Remove row of the dataframe
                # if this columns contains null value
                df = df.dropna(subset=[
                    'product_name',
                    'code',
                    'nutrition_grades',
                    'categories_hierarchy',
                    'ingredients',
                    'url',
                    'image_small_url',
                ])
                yield df
            except KeyError:
                pass

    def concat_dataframe(self):
        generator = self._generate_dataframe()
        return pd.concat([x for x in generator], ignore_index=True)
