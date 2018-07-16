from rest_framework import viewsets

from allergen.models import (Product, Allergen, Category,
                             Ingredient, Additive, Trace,
                             Nutriment, NutrimentComposeProduct)

from .serializers import (ProductSerializer, AllergenSerializer,
                                  CategorySerializer, IngredientSerializer,
                                  AdditiveSerializer, TraceSerializer,
                                  NutrimentSerializer, NutrimentComposeProductSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class AdditiveViewSet(viewsets.ModelViewSet):
    query = Additive.objects.all()
    serializer_class = AdditiveSerializer


class AllergenViewSet(viewsets.ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer


class TraceViewSet(viewsets.ModelViewSet):
    queryset = Trace.objects.all()
    serializer_class = TraceSerializer


class NutrimentViewSet(viewsets.ModelViewSet):
    queryset = Nutriment.objects.all()
    serializer_class = NutrimentSerializer


class NutrimentComposeProductViewSet(viewsets.ModelViewSet):
    queryset = NutrimentComposeProduct.objects.all()
    serializer_class = NutrimentComposeProductSerializer
