from rest_framework import viewsets

from allergen.models import Product

from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
