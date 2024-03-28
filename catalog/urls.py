from django.urls import path

from .apps import MainConfig
from .views import *

app_name = MainConfig.name

urlpatterns = [
    path('', home_cont, name='home'),
    path('contacts/', contacts_cont),
    path('sin_prod/<int:prod_id>', sin_prod),  # маршрут для вывода продукта по индексу
    path('new_prod/', new_prod)
]