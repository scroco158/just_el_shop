from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта', **NULLABLE)
    picture = models.ImageField(upload_to='product_picture/', verbose_name='Фото продукта', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.FloatField(verbose_name='Стоимость продукта')
    created_at = models.DateField(verbose_name='Дата создания продукта', **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата изменения продукта', **NULLABLE)
    product_owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='product_owner', **NULLABLE)
    is_moderated = models.BooleanField(default=False, verbose_name='Прошел модерацию')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
