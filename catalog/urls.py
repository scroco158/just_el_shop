from django.urls import path

from .apps import MainConfig
from .views import *

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts_cont),
    path('one_product/<int:pk>', ProductDetailView.as_view(), name='one_product'),
]