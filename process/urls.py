from django.urls import path
from .views import GoalListCreate, ProductListCreate, ProductDetailUpdate, ContractUploadView

urlpatterns = [
    path('goals/', GoalListCreate.as_view(), name='goal-list'),
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailUpdate.as_view(), name='product-detail'),
    path('contracts/upload/', ContractUploadView.as_view(), name='contract-upload'),
]
