from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product

# def contacts_cont(requests):
#
#     if requests.method == 'POST':
#         name = requests.POST.get('name')
#         phone = requests.POST.get('phone')
#         message = requests.POST.get('message')
#
#         print(f'name -> {name}\n '
#               f'phone -> {phone}\n'
#               f'message -> {message}\n')
#
#     return render(requests, 'catalog/contacts.html')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):  # ----_list.html
    model = Product


class ProductDetailView(DetailView):  # ---_detail.html
    model = Product
