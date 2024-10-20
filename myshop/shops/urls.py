from django.urls import path
from .views import ShopCreateView, ShopSearchView

urlpatterns = [
    path('', ShopSearchView.as_view(), name='shop-search'),  # For searching shops
    path('create/', ShopCreateView.as_view(), name='shop-create'),  # For creating shops
]
