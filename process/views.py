from rest_framework import viewsets

from process.models import Bus, Product
from process.serializers import ProcessSerializer, ProductSerializer


class ProcessViewSet(
    viewsets.ModelViewSet
):
    queryset = Bus.objects.all()
    serializer_class = ProcessSerializer
    lookup_field = 'id'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
