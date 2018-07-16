from rest_framework import serializers

from allergen.models import (Additive, Allergen, Category, Ingredient,
                             Nutriment, NutrimentComposeProduct, Product,
                             Trace, Translation, Vitamin)


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
        fields = ('nutriment_name',)


class NutrimentComposeProductSerializer(serializers.ModelSerializer):
    product_id = serializers.ReadOnlyField(source='product.id')
    nutriment_id = serializers.ReadOnlyField(source='nutriment.id')
    nutriment_quantity = serializers.ReadOnlyField(source='NutrimentComposeProduct.nutriment_quantity')

    class Meta:
        model = NutrimentComposeProduct
        fields = ('product_id', 'nutriment_id', 'nutriment_quantity',)


class ProductSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(many=True)
    additives = AdditiveSerializer(many=True)
    traces = TraceSerializer(many=True)
    nutriments = NutrimentSerializer(many=True)

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
                  'allergens',
                  'additives',
                  'traces',
                  )


