from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    Additive,
    Allergen,
    Category,
    Ingredient,
    Nutriment,
    NutrimentComposeProduct,
    Product,
    Trace,
    Vitamin,
    VitaminComposeProduct,
    Profile,
)


class CategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 0
    verbose_name_plural = "Categories"


class AdditiveInline(admin.TabularInline):
    model = Product.additives.through
    extra = 0
    verbose_name_plural = "Additifs"


class VitaminInline(admin.TabularInline):
    model = VitaminComposeProduct
    extra = 0
    verbose_name_plural = "Vitamines"


class NutrimentInline(admin.TabularInline):
    model = NutrimentComposeProduct
    extra = 0
    verbose_name_plural = "Nutriments"


class IngredientInline(admin.TabularInline):
    model = Product.ingredients.through
    extra = 0
    verbose_name_plural = "Ingrédients"


class AllergenInline(admin.TabularInline):
    model = Product.allergens.through
    extra = 0
    verbose_name_plural = "Allergènes"


class TraceInline(admin.TabularInline):
    model = Product.traces.through
    extra = 0
    verbose_name_plural = "Traces"


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "barcode", "nutrition_grade")
    fields = ("product_name", "image_url", "url_off", "barcode", "nutrition_grade")
    inlines = [
        CategoryInline,
        AdditiveInline,
        VitaminInline,
        NutrimentInline,
        IngredientInline,
        AllergenInline,
        TraceInline,
    ]
    search_fields = ("product_name", "barcode")
    list_filter = ["nutrition_grade"]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing existing object
            return self.readonly_fields + (
                "product_name",
                "image_url",
                "url_off",
                "barcode",
                "nutrition_grade",
            )
        return self.readonly_fields


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ("category_name",)


@admin.register(Additive)
class AdditiveAdmin(admin.ModelAdmin):
    fields = ("additive_name", "description", "risk", "max_permissible_dose")
    ordering = ("additive_name",)

    # if an additive already exist we don't want to modify it
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing existing object
            return self.readonly_fields + ("additive_name",)
        return self.readonly_fields


@admin.register(Vitamin)
class VitaminAdmin(admin.ModelAdmin):
    fields = ("vitamin_name", "description", ("daily_quantity_m", "daily_quantity_f"))
    ordering = ("vitamin_name",)


@admin.register(Nutriment)
class NutrimentAdmin(admin.ModelAdmin):
    fields = ('nutriment_name', 'description', 'image', ('daily_quantity_m', 'daily_quantity_f'))
    ordering = ('nutriment_name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ("ingredient_name",)
    ordering = ("ingredient_name",)


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    fields = ("allergen_name",)
    ordering = ("allergen_name",)


@admin.register(Trace)
class TraceAdmin(admin.ModelAdmin):
    fields = ("name",)
    ordering = ("name",)


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
