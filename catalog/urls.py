from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_cont),
    path('contacts/', views.contacts_cont)
]