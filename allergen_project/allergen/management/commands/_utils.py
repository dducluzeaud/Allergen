import requests

import pandas as pd
from googletrans import Translator


def count_pages():
    """
    Count pages for a category
    :return: page_number, integer
    """
    url = 'https://fr.openfoodfacts.org/categorie/'
    url += 'Aliments et boissons à base de végétaux.json'
    json_file = requests.get(url).json()
    page_number = json_file['count'] // 20
    if json_file['count'] % 20 != 0:
        page_number += 1
    return page_number


def generate_products(page):
    """
    Query the api by category and by page
    :param page: integer that fetch the api at the page number
    :return products['products']: json data containing all informations
    """
    url = 'https://fr.openfoodfacts.org/categorie/'
    url += 'Aliments et boissons à base de végétaux/' + str(page) + '.json'
    products = requests.get(url).json()
    return products['products']


def make_translation(word):
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
        translator = Translator()
        # take the language indication
        language = get_language(word)
        # remove language indicator
        word = slice_language(word)
        # translate word to french
        return translator.translate(word, src=language, dest='fr').text


def detect_lang(word):
    translator = Translator()
    # detect language
    tr = translator.detect(word)
    return tr.lang


def slice_language(word):
    if len(word) > 3 and word[2] == ':':
        word = word[3:]
    return word


def get_language(word):
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


def generate_dataframe():
    nb_pages = count_pages() + 1
    for page in range(1, nb_pages):
        print(page)
        products = generate_products(page)
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
                'nutrient_levels',  # sugar , salt, fat, saturated-fat level
                'nutriments',  # list all nutriments
                'traces_hierarchy',  # list all traces of allergens
            ]]
            # Remove row of the dataframe if this columns contains null value
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


def concat_dataframe():
    generator = generate_dataframe()
    return pd.concat([x for x in generator], ignore_index=True)
