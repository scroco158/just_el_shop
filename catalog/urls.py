from django.urls import path

#  from catalog import views
#  from . import views
from .views import *


urlpatterns = [
    path('', home_cont),
    path('contacts/', contacts_cont)
]