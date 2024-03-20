from django.shortcuts import render

from catalog.models import Product


def home_cont(requests):
    return render(requests,'catalog/home.html')


def contacts_cont(requests):

    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')

        print(f'name -> {name}\n '
              f'phone -> {phone}\n'
              f'message -> {message}\n')

    return render(requests, 'catalog/contacts.html')


def sin_prod(request, prod_id):

    product = Product.objects.get(pk=prod_id)
    context = {
        'object': product
        }
    return render(request, 'catalog/single_product.html', context)
