from django.urls import include, path

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views

router = routers.DefaultRouter()
router.register(r"product", views.ProductViewSet, base_name="product")
router.register(r"category", views.CategoryViewSet, base_name="category")
router.register(r"ingredient", views.IngredientViewSet, base_name="ingredient")
router.register(r"allergen", views.AllergenViewSet, base_name="allergen")
router.register(r"additive", views.AdditiveViewSet, base_name="additive")
router.register(r"vitamin", views.VitaminViewSet, base_name="vitamin")
router.register(r"nutriment", views.NutrimentViewSet, base_name="nutriment")
router.register(r"profile", views.UserViewSet, base_name="profile")

schema_view = get_swagger_view(title="Allergen API")

urlpatterns = [
    path("", include(router.urls)),
    path("doc/", schema_view),
    # JWT auth
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
