from django.urls import path
from .apps import BlogConfig
from .views import *

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create_record'),
    path('', BlogListView.as_view(), name='list'),
    path('one_record/<int:pk>', BlogDetailView.as_view(), name='one_record'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='update_record'),
    ]