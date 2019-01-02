import uuid
from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField('nom du produit', max_length=255)
    image_url = models.URLField("lien de l'image", max_length=255)
    url_off = models.URLField('lien openfoodfacts', max_length=255)
    barcode = models.BigIntegerField('code barre', db_index=True, unique=True)
    nutrition_grade = models.CharField('nutriscore', max_length=1)
    quantity = models.CharField('quantité', max_length=255)
    categories = models.ManyToManyField('Category')
    additives = models.ManyToManyField('Additive')
    vitamins = models.ManyToManyField('Vitamin', through='VitaminComposeProduct')
    nutriments = models.ManyToManyField('Nutriment', through='NutrimentComposeProduct')
    ingredients = models.ManyToManyField('Ingredient')
    substitutes = models.ManyToManyField(
        'self', through='Substitute', through_fields=('origin', 'replacement'), symmetrical=False
    )
    allergens = models.ManyToManyField('Allergen')
    traces = models.ManyToManyField('Trace')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'produit'


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    hierarchy = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'catégorie'


class Additive(models.Model):
    class Risk(Enum):
        safe = (0, 'Sans risque')
        caution = (1, 'Avec modération')
        suspicious = (2, 'Douteux')
        to_avoid = (3, 'A éviter')
        toxic = (4, 'Toxique')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    additive_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    risk = models.IntegerField(choices=[x.value for x in Risk], null=True, blank=True)
    max_permissible_dose = models.CharField(max_length=255)

    def __str__(self):
        return self.additive_name

    class Meta:
        verbose_name = 'additif'


class Vitamin(models.Model):
    vitamin_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    daily_quantity_m = models.CharField(max_length=255)
    daily_quantity_f = models.CharField(max_length=255)

    def __str__(self):
        return self.vitamin_name

    class Meta:
        verbose_name = 'vitamine'


class VitaminComposeProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    vitamin = models.ForeignKey('Vitamin', on_delete=models.SET_NULL, null=True)
    vitamin_quantity = models.DecimalField(max_digits=12, decimal_places=6)


class Nutriment(models.Model):
    nutriment_name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    daily_quantity_m = models.CharField(max_length=255)
    daily_quantity_f = models.CharField(max_length=255)

    def __str__(self):
        return self.nutriment_name


class NutrimentComposeProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    nutriment = models.ForeignKey('Nutriment', on_delete=models.SET_NULL, null=True)
    nutriment_quantity = models.DecimalField(max_digits=12, decimal_places=6)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = 'ingrédient'


class Allergen(models.Model):
    allergen_name = models.CharField(max_length=255)

    def __str__(self):
        return self.allergen_name

    class Meta:
        verbose_name = 'allergène'


class Trace(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Substitute(models.Model):
    origin = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='origin', verbose_name='produit original'
    )
    replacement = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='replacement',
        verbose_name='produit de substitution',
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='utilisateur')

    def __str__(self):
        return str({"origin": self.origin, "replacement": self.replacement, "user": self.user})

    class Meta:
        verbose_name = 'Substitut'


class Profile(models.Model):
    class Sexe(Enum):
        male = ('m', 'Homme')
        female = ('f', 'Femme')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    sexe = models.CharField(max_length=1, choices=[x.value for x in Sexe])
    height = models.IntegerField('taille')
    weight = models.IntegerField('poids')
    age = models.IntegerField('âge')
    basal_metabolism = models.IntegerField('métabolisme basal')
    ingredients = models.ManyToManyField('Ingredient')
    products = models.ManyToManyField('Product')
    allergens = models.ManyToManyField('Allergen')
    traces = models.ManyToManyField('Trace')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class SearchHistoric(models.Model):
    search_term = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.search_term

    class Meta:
        verbose_name = 'Historique de recherche'
        ordering = ['-date']


class Translation(models.Model):
    name_origin = models.CharField(max_length=255)
    translated_name = models.CharField(max_length=255)
    language = models.CharField(max_length=2, default='fr')
