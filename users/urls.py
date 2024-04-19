from django.contrib.auth.views import LoginView
from django.urls import path
from .apps import UsersConfig
from .views import *

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

]
