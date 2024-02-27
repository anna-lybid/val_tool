from django.urls import path, include

from rest_framework import routers

from process.views import ProcessViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register("process", ProcessViewSet, basename="process")
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls))
]

app_name = 'process'
