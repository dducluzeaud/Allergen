from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from api import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet, base_name='product')
router.register(r'category', views.CategoryViewSet, base_name='category')
router.register(r'ingredient', views.IngredientViewSet, base_name='ingredient')
router.register(r'allergen', views.AllergenViewSet, base_name='allergen')
router.register(r'additive', views.AdditiveViewSet, base_name='additive')
router.register(r'vitamin', views.VitaminViewSet, base_name='vitamin')

schema_view = get_swagger_view(title='Allergen API')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('doc/', schema_view),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))

]
