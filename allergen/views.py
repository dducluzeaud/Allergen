from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Additive, Allergen, Category, Ingredient, Nutriment, Product, Vitamin, Profile

from .serializers import (
    AdditiveSerializer,
    AllergenSerializer,
    CategorySerializer,
    IngredientSerializer,
    NutrimentSerializer,
    ProductSerializer,
    VitaminSerializer,
    ProfileSerializer,
    UserSerializer,
)


class ProductViewSet(ModelViewSet):
    """
    API endpoint that allows products to be viewed.

    Can be filtered and ordered by product_name, barcode, or nutrition_grade.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ("product_name", "barcode", "nutrition_grade")
    ordering = "nutrition_grade"
    ordering_fields = ("product_name", "barcode", "nutrition_grade")
    http_method_names = ["get"]


class CategoryViewSet(ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ("category_name",)
    http_method_names = ["get"]


class IngredientViewSet(ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed.
    """

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ("ingredient_name",)
    http_method_names = ["get"]


class AdditiveViewSet(ModelViewSet):
    """
    API endpoint that allows additives to be viewed.

    Can be filtered by additive_name or risk.
    Can be ordered by risk, but is by default ordered by additive_name.
    """

    queryset = Additive.objects.all()
    serializer_class = AdditiveSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ("additive_name", "risk")
    ordering = "additive_name"
    ordering_fields = ("risk", "additive_name")
    http_method_names = ["get"]


class AllergenViewSet(ModelViewSet):
    """
    API endpoint that allows allergens to be viewed.
    """

    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ("allergen_name",)
    http_method_names = ["get"]


class VitaminViewSet(ModelViewSet):
    """
    API endpoint that allows vitamins to be viewed.
    """

    queryset = Vitamin.objects.all()
    serializer_class = VitaminSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering = ("vitamin_name",)
    http_method_names = ["get"]


class NutrimentViewSet(ModelViewSet):
    queryset = Nutriment.objects.all()
    serializer_class = NutrimentSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.query_params('username')
        return User.objects.filter(username=user)
