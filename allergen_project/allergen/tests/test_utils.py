import requests
import requests_mock
from django.test import TestCase

from allergen.management.commands._utils import (ProductDataFrame, DataTranslation,
                                                 normalize_value)


class TestNormalizeValue(TestCase):
    def test_value(self):
        """Test if the value is correct else its returned 0.0"""
        correct_value = 12
        incorrect_value = 'False'
        incorrect_value_2 = False
        self.assertEqual(normalize_value(correct_value, 'mg'), 12)
        self.assertEqual(normalize_value(incorrect_value, 'mg'), 0.0)
        self.assertEqual(normalize_value(incorrect_value_2, 'mg'), 0.0)

    def test_unit(self):
        """Test if the unit is correctly informed else it should returned 0.0"""
        value = 12
        unit_mg = 'mg'
        incorrect_unit_1 = 'kc'
        incorrect_unit_2 = 12
        incorrect_unit_3 = ' '
        incorrect_unit_4 = False
        incorrect_unit_5 = 1.0
        self.assertEqual(normalize_value(value, unit_mg), 12)
        self.assertEqual(normalize_value(value, incorrect_unit_1), 0.0)
        self.assertEqual(normalize_value(value, incorrect_unit_2), 0.0)
        self.assertEqual(normalize_value(value, incorrect_unit_3), 0.0)
        self.assertEqual(normalize_value(value, incorrect_unit_4), 0.0)
        self.assertEqual(normalize_value(value, incorrect_unit_5), 0.0)

    def test_normalization(self):
        """Test if the value is returned in mg or kcal or ml."""
        value = 12
        unit_mg = 'mg'
        unit_kcal = 'kcal'
        unit_ml = 'ml'
        unit_kg = 'kg'
        unit_g = 'g'
        unit_µg = 'µg'
        unit_kj = 'kj'
        unit_L = 'L'
        unit_µL = 'µL'
        self.assertEqual(normalize_value(value, unit_mg), value)
        self.assertEqual(normalize_value(value, unit_kcal), value)
        self.assertEqual(normalize_value(value, unit_ml), value)
        self.assertEqual(normalize_value(value, unit_kg), value * 1000000)
        self.assertEqual(normalize_value(value, unit_g), value * 1000)
        self.assertEqual(normalize_value(value, unit_µg), value / 1000)
        self.assertEqual(normalize_value(value, unit_kj), value * 239.005)
        self.assertEqual(normalize_value(value, unit_L), value * 1000)
        self.assertEqual(normalize_value(value, unit_µL), value / 1000)


class TestTranslation(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.tr = DataTranslation()

    def test_detect_lang(self):
        word = 'en:bonjour'
        word_en = 'hello'
        word_fr = 'bonjour'
        not_word = 'abcdefghij'
        self.assertEqual(self.tr.detect_lang(word), 'fr')
        self.assertEqual(self.tr.detect_lang(word_en), 'en')
        self.assertEqual(self.tr.detect_lang(word_fr), 'fr')
        self.assertFalse(self.tr.detect_lang(not_word))

    def test_slice_language(self):
        word = 'en:hello'
        word_2 = 'hello'
        self.assertEqual(self.tr.slice_language(word_2), word_2)
        self.assertEqual(self.tr.slice_language(word), word_2)
        self.assertNotEqual(self.tr.slice_language(word), word)

    def test_get_language(self):
        word = 'en:bonjour'
        word_en = 'hello'
        word_fr = 'Bonjour'
        not_word = 'abcdefghij'
        self.assertEqual(self.tr.get_language(word), 'fr')
        self.assertEqual(self.tr.get_language(word_en), 'en')
        self.assertEqual(self.tr.get_language(word_fr), 'fr')
        self.assertFalse(self.tr.get_language(not_word))

    def test_make_translation(self):
        word = 'en:Bonjour'
        word_en = 'hello'
        word_fr = 'Bonjour'
        not_word = 'abcdefghij'
        self.assertEqual(self.tr.make_translation(word), 'Bonjour')
        self.assertEqual(self.tr.make_translation(word_en), 'Bonjour')
        self.assertEqual(self.tr.make_translation(word_fr), 'Bonjour')
        self.assertFalse(self.tr.make_translation(not_word))


@requests_mock.Mocker()
class TestProductDataFrame(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = 'Aliments et boissons à base de végétaux'
        cls.data = ProductDataFrame(cls.category)
        
    def setUp(self):
        self.mock_url = f'https://fr.openfoodfacts.org/categorie/'
        self.mock_url += f'Aliments%20et%20boissons%20%C3%A0%20base%20de%20v%C3%A9g%C3%A9taux'


    def test_count_pages(self, m):
        self.mock_url += '.json'
        m.register_uri('GET', self.mock_url, json={'count': 34}, status_code=200)
        self.assertEqual(self.data._count_pages(), 2)

    def test_generate_products(self, m):
        self.mock_url += '/1.json'
        m.register_uri(
            'GET',
            self.mock_url,
            json={
                "page_size": 20,
                "skip": 0,
                "count": 1,
                "products": [
                    {
                        "product_name": "test"
                    },
                    {
                        "product_name": "test_2"
                    }]},
                    status_code=200
                )
        self.assertEqual(
            self.data._generate_products(1), 
            [
                {
                    "product_name": "test"
                },
                {
                    "product_name": "test_2"
                }]
            )

    def test_generate_products(self):
        
