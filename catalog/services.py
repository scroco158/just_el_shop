from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """" Возвращает категории товаров или из кэша, или из БД"""

    if not CACHE_ENABLED:
        return Category.objects.all()

    key = 'cats_list'
    cats = cache.get(key)
    if cats is not None:
        return cats

    cats = Category.objects.all()
    cache.set(key, cats)

    return cats
