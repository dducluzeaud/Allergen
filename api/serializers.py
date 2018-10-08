from rest_framework import serializers

from allergen.models import (Additive, Allergen, Category, Ingredient,
                             Nutriment, NutrimentComposeProduct, Product,
                             Trace, Translation, Vitamin, VitaminComposeProduct)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('ingredient_name',)


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ('allergen_name',)


class AdditiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additive
        fields = ('additive_name', 'risk', 'description')


class TraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trace
        fields = ('name',)


class NutrimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutriment
        fields = ('nutriment_name', 'description', 'daily_quantity_m', 'daily_quantity_f', )


class NutrimentComposeProductSerializer(serializers.HyperlinkedModelSerializer):
    nutriment_name = serializers.ReadOnlyField(
        source='nutriment.nutriment_name')

    class Meta:
        model = NutrimentComposeProduct
        fields = ('nutriment_name', 'nutriment_quantity',)


class VitaminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamin
        fields = ('vitamin_name', 'description', 'daily_quantity_m', 'daily_quantity_f', )


class VitaminComposeProductSerializer(serializers.HyperlinkedModelSerializer):
    vitamin_name = serializers.ReadOnlyField(source='vitamin.vitamin_name')

    class Meta:
        model = VitaminComposeProduct
        fields = ('vitamin_name', 'vitamin_quantity',)


class ProductSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True)
    categories = CategorySerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    additives = AdditiveSerializer(many=True)
    traces = TraceSerializer(many=True)
    nutriments = NutrimentComposeProductSerializer(
        source='nutrimentcomposeproduct_set', many=True)
    vitamins = VitaminComposeProductSerializer(
        source='vitamincomposeproduct_set', many=True)

    class Meta:
        model = Product
        fields = ('product_name',
                  'image_url',
                  'url_off',
                  'barcode',
                  'nutrition_grade',
                  'quantity',
                  'categories',
                  'ingredients',
                  'nutriments',
                  'vitamins',
                  'additives',
                  'allergens',
                  'traces',
                  )
