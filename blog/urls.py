from django.urls import path
from .apps import BlogConfig
from .views import *

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create_record'),
]