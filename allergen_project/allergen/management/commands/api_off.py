from allergen.models import (Additive, Allergen, Category, Ingredient,
                             Nutriment, NutrimentComposeProduct, Product,
                             Trace, Translation, Vitamin, VitaminComposeProduct)

from django.core.management.base import BaseCommand

from ._utils import (concat_dataframe, get_language,
                     make_translation, slice_language)

import re


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
            ingredients = data.loc[index, 'ingredients']
            nutriments = data.loc[index, 'nutriments']
            traces_hierarchy = data.loc[index, 'traces_hierarchy']

            prod, prod_created = Product.objects.get_or_create(
                barcode=code,
                defaults={
                    'product_name': product_name,
                    'image_url': image_small_url,
                    'url_off': url,
                    'nutrition_grade': nutrition_grades,
                    'quantity': quantity,
                })

            if not prod_created:
                pass
            else:
                cat_length = len(categories_hierarchy)
                for i in range(cat_length):
                    category = categories_hierarchy[i]
                    # Search if the french traduction has already been made
                    # otherwise make and insert the traduction
                    language = get_language(category)

                    trans_category, created = Translation.objects.get_or_create(
                        name_origin=slice_language(category),
                        defaults={
                            'translated_name': make_translation(category),
                            'language': language
                        }
                    )
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
                    additive = slice_language(additive)
                    # additives a re always form with letter e and 3-4 digits
                    regex = re.compile(r"^(e|E)[0-9]{3,4}")
                    match = re.search(regex, additive)
                    if match:
                        add, add_created = Additive.objects.get_or_create(
                            additive_name=match[0])

                        # add additive to the product
                        prod.additives.add(add)
                    else:
                        continue

                for ingredient in ingredients:

                    # ingredient might have a language indicator
                    ingredient = ingredient['text']
                    ing, ing_created = Ingredient.objects.get_or_create(
                        ingredient_name=ingredient
                    )
                    # add ingredient to product
                    prod.ingredients.add(ing)

                for allergen in allergens_hierarchy:
                    language = get_language(allergen)

                    t_all, t_all_created = Translation.objects.get_or_create(
                        name_origin=slice_language(allergen),
                        defaults={
                            'translated_name': make_translation(allergen),
                            'language': language
                        })
                    # Insert in the database if the category does not exists
                    alg, alg_created = Allergen.objects.get_or_create(
                        allergen_name=t_all.translated_name)

                    # Add relation to the product
                    NutrimentComposeProduct.objects.create

                for trace in traces_hierarchy:
                    lang = get_language(trace)

                    t_tra, t_tra_created = Translation.objects.get_or_create(
                        name_origin=slice_language(trace),
                        defaults={
                            'translated_name': make_translation(trace),
                            'language': lang
                        })
                    # Insert in the database if the category does not exists
                    tra, tra_created = Trace.objects.get_or_create(
                        name=t_tra.translated_name)

                    prod.traces.add(tra)

                for k, v in nutriments.items():
                    if k == 'energy_value':
                        ene, ene_c = Nutriment.objects.get_or_create(
                            nutriment_name='énergie'
                        )

                        quantity = ' '.join([str(nutriments['energy_value']),
                                            nutriments['energy_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=ene,
                            nutriment_quantity=quantity
                        )

                    elif k == 'fat_value':
                        fat, fat_c = Nutriment.objects.get_or_create(
                            nutriment_name='graisses'
                        )

                        quantity = ' '.join([str(nutriments['fat_value']),
                                            nutriments['fat_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=fat,
                            nutriment_quantity=quantity
                        )
                    elif k == 'protein_value':
                        pro, pro_c = Nutriment.objects.get_or_create(
                            nutriment_name='protéines'
                        )

                        quantity = ' '.join([str(nutriments['protein_value']),
                                            nutriments['protein_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=pro,
                            nutriment_quantity=quantity
                        )
                    elif k == 'salt_value':
                        salt, salt_c = Nutriment.objects.get_or_create(
                            nutriment_name='sel'
                        )

                        quantity = ' '.join([str(nutriments['salt_value']),
                                            nutriments['salt_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=salt,
                            nutriment_quantity=quantity
                        )
                    elif k == 'sugar_value':
                        sugar, sugar_c = Nutriment.objects.get_or_create(
                            nutriment_name='sucre'
                        )

                        quantity = ' '.join([str(nutriments['sugar_value']),
                                            nutriments['sugar_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=sugar,
                            nutriment_quantity=quantity
                        )
                    elif k == 'saturated_fat_value':
                        sat_fat, sat_fat_c = Nutriment.objects.get_or_create(
                            nutriment_name='graisses saturés'
                        )

                        quantity = ' '.join([str(nutriments['saturated_fat_value']),
                                            nutriments['saturated_fat_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=sat_fat,
                            nutriment_quantity=quantity
                        )

                    elif k == 'polyunsaturated-fat_label':
                        poly, poly_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )
                        quantity = ' '.join([str(nutriments['polyunsaturated-fat_value']),
                                            nutriments['polyunsaturated-fat_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=poly,
                            nutriment_quantity=quantity
                        )

                    elif k == 'monounsaturated-fat_label':
                        mono, mono_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['monounsaturated-fat_value']),
                                            nutriments['monounsaturated-fat_unit']])
                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=mono,
                            nutriment_quantity=quantity
                        )

                    elif k == 'omega-3-fat_label':
                        om3, om3_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['omega-3-fat_value']),
                                            nutriments['omega-3-fat_unit']])
                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=om3,
                            nutriment_quantity=quantity
                        )

                    elif k == 'omega-6-fat_label':
                        om6, om6_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['omega-6-fat_value']),
                                            nutriments['omega-6-fat_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=om6,
                            nutriment_quantity=quantity
                        )

                    elif k == 'omega-9-fat_label':
                        om9, om9_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['omega-9-fat_value']),
                                            nutriments['omega-9-fat_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=om9,
                            nutriment_quantity=quantity
                        )

                    # Calcium
                    elif k == 'calcium_label':
                        cal, cal_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['calcium_value']),
                                            nutriments['calcium_label']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=cal,
                            nutriment_quantity=quantity
                        )

                    # Cholesterol
                    elif k == 'cholesterol_label':
                        cho, cho_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['cholesterol_value']),
                                            nutriments['cholesterol_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=cho,
                            nutriment_quantity=quantity
                        )
                    # Fer
                    elif k == 'iron_label':
                        iro, iro_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['iron_value']),
                                            nutriments['iron_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=iro,
                            nutriment_quantity=quantity
                        )

                    # Fibres
                    elif k == 'fiber_label':
                        fib, fib_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['fiber_value']),
                                            nutriments['fiber_unit']])
                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=fib,
                            nutriment_quantity=quantity
                        )

                    # Fructose
                    elif k == 'fructose_label':
                        fru, fru_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['fructose_value']),
                                            nutriments['fructose_unit']])
                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=fru,
                            nutriment_quantity=quantity
                        )

                    # gluten
                    elif k == 'gluten_label':
                        glu, glu_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['gluten_value']),
                                            nutriments['gluten_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=glu,
                            nutriment_quantity=quantity
                        )

                    # Lactose
                    elif k == 'lactose_label':
                        lac, lac_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['lactose_value']),
                                            nutriments['lactose_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=lac,
                            nutriment_quantity=quantity
                        )

                    # Magnesium
                    elif k == 'magnesium_label':
                        mag, mag_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['magnesium_value']),
                                            nutriments['magnesium_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=mag,
                            nutriment_quantity=quantity
                        )

                    # Potassium
                    elif k == 'potassium_label':
                        pot, pot_c = Nutriment.objects.get_or_create(
                            nutriment_name=v
                        )

                        quantity = ' '.join([str(nutriments['potassium_value']),
                                            nutriments['potassium_unit']])

                        NutrimentComposeProduct.objects.create(
                            product=prod,
                            nutriment=pot,
                            nutriment_quantity=quantity
                        )

                # Vitamim
                    # A
                    elif k == 'beta-carotene_label':
                        bet, bet_c = Vitamin.objects.get_or_create(
                            vitamin_name='beta-carotène'
                        )

                        quantity = ' '.join([str(nutriments['beta-carotene_value']),
                                            nutriments['beta-carotene_unit']])

                        VitaminComposeProduct.objects.create(
                            product=prod,
                            vitamin=bet,
                            vitamin_quantity=quantity
                        )

                    elif k == 'vitamin-a_label':
                        vit_a, vit_a_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine A'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-a_value']),
                                            nutriments['vitamin-a_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_a,
                            vitamin_quantity=quantity
                        )

                    elif k == 'carotene_label':
                        car, car_c = Vitamin.objects.get_or_create(
                            vitamin_name='carotène'
                        )

                        quantity = ' '.join([str(nutriments['carotene__value']),
                                            nutriments['carotene__unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=car,
                            vitamin_quantity=quantity
                        )

                    # B1
                    elif k == 'vitamin-b1_label':
                        vit_b1, vit_b1_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B1'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-b1_value']),
                                            nutriments['vitamin-b1_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b1,
                            vitamin_quantity=quantity
                        )


                    # B2
                    elif k == 'vitamin-b2_label':
                        vit_b2, vit_b2_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B2'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-b2_value']),
                                            nutriments['vitamin-b2_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b2,
                            vitamin_quantity=quantity
                        )

                    # B3
                    elif k == 'vitamin-pp_label':
                        vit_pp, vit_pp_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B3'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-pp_value']),
                                            nutriments['vitamin-pp_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_pp,
                            vitamin_quantity=quantity
                        )

                    # B5
                    elif k == 'pantothenic-acid_label':
                        vit_b5, vit_b5_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B5'
                        )

                        quantity = ' '.join([str(nutriments['pantothenic-acid_value']),
                                            nutriments['pantothenic-acid_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b5,
                            vitamin_quantity=quantity
                        )

                    # B6
                    elif k == 'vitamin-b6_label':
                        vit_b6, vit_b6_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B6'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-b6_value']),
                                            nutriments['vitamin-b6_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b6,
                            vitamin_quantity=quantity
                        )

                    # B8
                    elif k == 'biotin_label':
                        vit_b8, vit_b8_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B8'
                        )

                        quantity = ' '.join([str(nutriments['biotin_value']),
                                            nutriments['biotin_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b8,
                            vitamin_quantity=quantity
                        )

                    # B9
                    elif k == 'vitamin-b9_label':
                        vit_b9, vit_b9_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B9'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-b9_value']),
                                            nutriments['vitamin-b9_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b9,
                            vitamin_quantity=quantity
                        )

                    # B12
                    elif k == 'vitamin-b12_label':
                        vit_b12, vit_b12_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine B12'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-b12_value']),
                                            nutriments['vitamin-b12_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_b12,
                            vitamin_quantity=quantity
                        )

                    # C
                    elif k == 'vitamin-c_label':
                        vit_c, vit_c_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine C'
                        )
                        try:
                            quantity = ' '.join([str(nutriments['vitamin-c_value']),
                                                    nutriments['vitamin-c_unit']])

                            VitaminComposeProduct.objects.get_or_create(
                                product=prod,
                                vitamin=vit_c,
                                vitamin_quantity=quantity
                            )
                        except KeyError:
                            pass

                    # D
                    elif k == 'vitamin-d_label':
                        vit_d, vit_d_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine D'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-d_value']),
                                            nutriments['vitamin-d_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_d,
                            vitamin_quantity=quantity
                        )

                    # E
                    elif k == 'vitamin-e_label':
                        vit_e, vit_e_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine E'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-e_value']),
                                            nutriments['vitamin-e_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_e,
                            vitamin_quantity=quantity
                        )

                    # K
                    elif k == 'vitamin-k_label':
                        vit_k, vit_k_c = Vitamin.objects.get_or_create(
                            vitamin_name='vitamine K'
                        )

                        quantity = ' '.join([str(nutriments['vitamin-k_value']),
                                            nutriments['vitamin-k_unit']])

                        VitaminComposeProduct.objects.get_or_create(
                            product=prod,
                            vitamin=vit_k,
                            vitamin_quantity=quantity
                        )
