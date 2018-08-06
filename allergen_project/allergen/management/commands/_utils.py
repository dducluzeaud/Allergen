from typing import List, Iterator, Union

import pandas as pd
import requests
import string
from googletrans import Translator

from .languages import LANGCODES


def normalize_value(value: float, unit: str) -> float:
    """Convert all value to mg, mL or kcal."""
    try:
        value = float(value)
    # if value can't be cast the value must be incorrect
    # return 0
        if unit.lower() == 'mg' or unit.lower() == 'kcal' or unit.lower() == 'ml':
            return value
        elif unit.lower() == 'kg':
            value = value * 1000000
        elif unit.lower() == 'g':
            value = value * 1000
        elif unit.lower() == 'µg':
            value = value / 1000
        elif unit.lower() == 'kj':
            value = value * 239.005
        elif unit.lower() == 'l':
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
    except AttributeError:
        return 0.0


class DataTranslation:

    def __init__(self) -> None:
        self.translator = Translator()

    def make_translation(self, word: str) -> Union[bool, str]:
        """
        Translate a word using GoogleTrans library
        The language might be indicate in the 2 first character
        :param word: string
        :param language: string
        :return: word string, or False if the word can't be translated
        """
        if word == 'en:spreads':
            # better translation for the word spreads
            return 'Pate à tartiner'
        elif word == 'en:sweets-spreads':
            return 'Pâte à tartiner sucrée'
        elif word == 'en:plant-based-spreads':
            return 'Pâte à tartiner végétal'
        elif word == ' ':
            return False
        else:
            # take the language indication
            language = self.get_language(word)
            if not language:
                return False
            else:
                # remove language indicator
                word = self.slice_language(word)
                # translate word to french
                word = self.translator.translate(
                    word,
                    src=language,
                    dest='fr'
                ).text
                # remove any type of punctuation
                return word.replace('-', ' ')

    def detect_lang(self, word: str) -> Union[bool, str]:
        """Detect language with googletrans"""
        # detect language
        tr = self.translator.detect(word)
        if tr.confidence < 0.5:
            return False
        else:
            for l in LANGCODES.values():
                if tr.lang == l:
                    return tr.lang
            return False

    def slice_language(self, word: str) -> str:
        if len(word) > 3 and word[2] == ':':
            return word[3:]
        return word

    def get_language(self, word: str) -> str:
        """
        Return the language of the word if its has a language indicator.
        If its has not googletrans library will detect its language
        """
        if len(self.slice_language(word)) == len(word):
            # the word has no language indicator
            lang = self.detect_lang(word)
        else:
            lang = word[:2]
            tr = self.translator.detect(word)
            # if language detected is different
            # the confidence of the translator is above 90 %
            # take the language from the translator
            if tr.confidence > 0.9 and tr.lang != lang:
                lang = tr.lang
        return lang


class ProductDataFrame:
    """
    Generate a dataframe concatenating all pages founds related to
    the category on openfoodfacts.
    """

    def __init__(self, category: str) -> None:
        self.category = category

    def _count_pages(self) -> int:
        """
        Count pages for a category
        :return: page_number, integer
        """
        url = 'https://fr.openfoodfacts.org/categorie/'
        url += f'{self.category}.json'
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
        url += f'{self.category}/{str(page)}.json'
        products = requests.get(url).json()
        return products['products']

    def _generate_dataframe(self) -> Iterator:
        """
        Query openfoodfacts and concatenate the dataframe
        for every page in the category. The dataframe select
        column and remove empty row if some values are missing
        in the column.
        """
        nb_pages = self._count_pages() + 1
        for page in range(1, 20):
            products = self._generate_products(page)
            df = pd.DataFrame(products)
            # Select columns from the dataframe
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

    def concat_dataframe(self) -> object:
        """Unpack the generator and concatenate all dataframe from it.
        
        Returns:
           Dataframe : dataframe with all value extracted by page.
        """

        generator = self._generate_dataframe()
        return pd.concat([x for x in generator], ignore_index=True)
