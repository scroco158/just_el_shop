from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из микстур с категориями

        with open('cat_data.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            return data

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами

        with open ('prod_data.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            return data

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()
        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []
        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(Category(pk=category['pk'],
                                                name=category['fields']['name'],
                                                description=category['fields']['description']))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(pk=product['pk'],
                                              name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              picture=product['fields']['picture'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
