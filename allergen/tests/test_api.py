from django.urls import include, path, reverse
from rest_framework import APITestCase, URLPatternsTestCase


class ProductTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('/api/product/', include(allergens.urls))
    ]

    def test_detail_product(self):
        pass

    def test_create_product(self):
        pass

    def test_list_product(self):
        pass
