from django.urls import path
from django.views.decorators.cache import cache_page
from .apps import MainConfig
from .views import ProductListView, ContactsView, ProductDetailView, ProductUpdateView, ProductCreateView, \
    ProductDeleteView, VersionCreateView, CategoryListView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('one_product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='one_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

    path('create_version/', VersionCreateView.as_view(), name='create_version'),

]
