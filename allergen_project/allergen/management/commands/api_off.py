import requests

from allergen.models import (Additive, Category, Ingredient,
                             Allergen, Trace, Nutriment,
                             NutrimentComposeProduct, Product, Profile,
                             SearchHistoric, Substitute, Translation, Vitamin,
                             VitaminComposeProduct)
from django.core.management.base import BaseCommand

from ._utils import concat_dataframe, make_translation, slice_language, detect_lang


class Command(BaseCommand):
    """
    Query the openfoodfacts api and insert or update products in the database.
    """

    def handle(self, *args, **kwargs):

        data = concat_dataframe()

        for index in data.index.values:
            """
            Fetch data in the dataframe
            """
            product_name = data.loc[index, 'product_name']
            code = data.loc[index, 'code']
            image_small_url = data.loc[index, 'image_small_url']
            url = data.loc[index, 'url']
            nutrition_grades = data.loc[index, 'nutrition_grades']
            quantity = data.loc[index, 'quantity']
            categories_hierarchy = data.loc[index, 'categories_hierarchy']
            additives_tags = data.loc[index, 'additives_tags']
            allergens_hierarchy = data.loc[index, 'allergens_hierarchy']
            ingredients_hierarchy = data.loc[index, 'ingredients_hierarchy']
            ingredients_n = data.loc[index, 'ingredients_n']
            nutrient_levels = data.loc[index, 'nutrient_levels']
            nutriments = data.loc[index, 'nutriments']
            traces_hierarchy = data.loc[index, 'traces_hierarchy']

            prod, prod_created = Product.objects.get_or_create(barcode=code,
                                                               defaults={
                                                                   'product_name': product_name,
                                                                   'image_url': image_small_url,
                                                                   'url_off': url,
                                                                   'nutrition_grade': nutrition_grades,
                                                                   'quantity': quantity,
                                                               })

            # Reverse the list and insert category by parent
            cat_length = len(categories_hierarchy)
            for i in range(cat_length):
                category = categories_hierarchy[i]
                # Search if the french traduction has arlready been made
                # otherwise make and insert the traduction
                if len(category) > 3 and category[2] == ':':
                    language = category[:2]
                else:
                    language = detect_lang(category)

                trans_category, created = Translation.objects.get_or_create(name_origin=slice_language(category),
                                                                            defaults={
                                                                                'translated_name': make_translation(category),
                                                                                'language': language
                })
                # Insert in the database if the category does not exists
                cat, created = Category.objects.get_or_create(
                    category_name=trans_category.translated_name)

                # Add relation to the product
                prod.categories.add(cat)

                # at least one category have been created
                if i >= 1:
                    parent_category = slice_language(
                        categories_hierarchy[i - 1])
                    trans_parent_category = Translation.objects.get(
                        name_origin=parent_category)
                    parent_category = Category.objects.get(
                        category_name=trans_parent_category.translated_name)
                    cat.hierarchy.add(parent_category)

            for additive in additives_tags:
                # additive might have a language indicator
                additive = make_translation(additive)
                add, add_created = Additive.objects.get_or_create(
                    additive_name=additive)

                # add additive to the product
                prod.additives.add(add)

            for ingredient in ingredients_hierarchy:
                # ingredient might have a language indicator
                ingredient = make_translation(ingredient, False)
                ing, ing_created = Ingredient.objects.get_or_create(
                    ingredient_name=ingredient
                )
                # add ingredient to product
                prod.ingredients.add(ing)

            for allergen in allergens_hierarchy:
                if len(allergen) > 3 and allergen[2] == ':':
                    language = allergen[:2]
                else:
                    language = detect_lang(allergen)

                t_all, t_all_created = Translation.objects.get_or_create(name_origin=slice_language(allergen),
                                                                         defaults={
                    'translated_name': make_translation(allergen),
                    'language': language
                })
                # Insert in the database if the category does not exists
                alg, alg_created = Allergen.objects.get_or_create(
                    allergen_name=t_all.translated_name)

                # Add relation to the product
                prod.allergen.create(alg)

            for trace in traces_hierarchy:
                if len(trace) > 3 and trace[2] == ':':
                    language = trace[:2]
                else:
                    language = detect_lang(trace)

                t_tra, t_tra_created = Translation.objects.get_or_create(name_origin=slice_language(trace),
                                                                         defaults={
                    'translated_name': make_translation(trace),
                    'language': language
                })
                # Insert in the database if the category does not exists
                tra, tra_created = Trace.objects.get_or_create(
                    name=t_tra.translated_name)

                # Add relation to the product
                prod.trace.create(alg)
