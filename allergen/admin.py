from django.contrib import admin

from .models import (
    Product,
    Category,
    Additive,
    Vitamin,
    VitaminComposeProduct,
    Nutriment,
    NutrimentComposeProduct,
    Ingredient,
    Allergen,
    Trace,
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "barcode", "nutrition_grade")
    fields = ("product_name", "image_url", "url_off",
              "barcode", "nutrition_grade")
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
    fields = ("vitamin_name", "description",
              ("daily_quantity_m", "daily_quantity_f"))
    ordering = ("vitamin_name",)


@admin.register(Nutriment)
class NutrimentAdmin(admin.ModelAdmin):
    fields = ("nutriment_name", "description",
              ("daily_quantity_m", "daily_quantity_f"))
    ordering = ("nutriment_name",)


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


@admin.register(NutrimentComposeProduct)
class NutrimentComposeProductAdmin(admin.ModelAdmin):
    fields = ("nutriment_quantity",)
    list_display = ("nutriment_quantity",)
    ordering = ("nutriment_quantity",)
