from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, ReadOnlyField

from django.contrib.auth.models import User

from .models import (
    Additive,
    Allergen,
    Category,
    Ingredient,
    Nutriment,
    NutrimentComposeProduct,
    Product,
    Profile,
    Trace,
    Vitamin,
    VitaminComposeProduct,
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("category_name",)


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("ingredient_name",)


class AllergenSerializer(ModelSerializer):
    class Meta:
        model = Allergen
        fields = ("allergen_name",)


class AdditiveSerializer(ModelSerializer):
    class Meta:
        model = Additive
        fields = ("additive_name", "risk", "description")


class TraceSerializer(ModelSerializer):
    class Meta:
        model = Trace
        fields = ("name",)


class NutrimentSerializer(ModelSerializer):
    class Meta:
        model = Nutriment
        fields = ("id", "nutriment_name", "description", "daily_quantity_m", "daily_quantity_f")


class NutrimentComposeProductSerializer(HyperlinkedModelSerializer):
    nutriment_name = ReadOnlyField(source="nutriment.nutriment_name")

    class Meta:
        model = NutrimentComposeProduct
        fields = ("nutriment_name", "nutriment_quantity")


class VitaminSerializer(ModelSerializer):
    class Meta:
        model = Vitamin
        fields = ("vitamin_name", "description", "daily_quantity_m", "daily_quantity_f")


class VitaminComposeProductSerializer(HyperlinkedModelSerializer):
    vitamin_name = ReadOnlyField(source="vitamin.vitamin_name")

    class Meta:
        model = VitaminComposeProduct
        fields = ("vitamin_name", "vitamin_quantity")


class ProductSerializer(ModelSerializer):
    allergens = AllergenSerializer(many=True)
    categories = CategorySerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    additives = AdditiveSerializer(many=True)
    traces = TraceSerializer(many=True)
    nutriments = NutrimentComposeProductSerializer(source="nutrimentcomposeproduct_set", many=True)
    vitamins = VitaminComposeProductSerializer(source="vitamincomposeproduct_set", many=True)

    class Meta:
        model = Product
        fields = (
            "product_name",
            "image_url",
            "url_off",
            "barcode",
            "nutrition_grade",
            "quantity",
            "categories",
            "ingredients",
            "nutriments",
            "vitamins",
            "additives",
            "allergens",
            "traces",
        )


class ProfileSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    allergens = AllergenSerializer(many=True)

    class Meta:
        model = Profile
        fields = ("ingredients", "products", "allergens")


class UserSerializer(HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "profile")
