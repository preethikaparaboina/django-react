from django.urls import path
from .views import (
    UserIDView,
    ItemListView,
    ItemDetailView,
    
)

urlpatterns = [
    path('user-id/', UserIDView.as_view(), name='user-id'),
    path('products/', ItemListView.as_view(), name='product-list'),
    path('products/<pk>/', ItemDetailView.as_view(), name='product-detail'),
    

]
