from django.urls import path

from .apps import MainConfig
from .views import *

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('one_product/<int:pk>', ProductDetailView.as_view(), name='one_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),

]