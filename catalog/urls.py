from django.urls import path

#  from catalog import views
#  from . import views
from .views import *


urlpatterns = [
    path('', home_cont),
    path('contacts/', contacts_cont),
    path('sin_prod/<int:prod_id>', sin_prod),  # маршрут для вывода продукта по индексу
    path('new_prod/', new_prod)
]