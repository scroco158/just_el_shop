from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email Address", max_length=255,
                              help_text='Required. Inform a valid email address.')
    phone_number = models.CharField(max_length=35, verbose_name="Phone Number",
                                    help_text='Required. Inform a valid phone number.', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name="Country",
                               help_text='Required. Inform a valid country.', **NULLABLE)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Avatar",
                               help_text="Upload your avatar.", ** NULLABLE)
    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['email']

    def __str__(self):
        return self.email
