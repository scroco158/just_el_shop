from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Version


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ver = Version.objects.filter(product=self.object)  # выборка всех версий текущего продукта
        v_pr = []
        for v in ver:
            v_pr.append(v.name)
            print(v.name)
        print(v_pr)
        context['v_pr'] = v_pr

        return context


class ProductUpdateView(UpdateView):  # ---_form.html
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):  # ---_form.html
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):  # ---_confirm_delete.html
    model = Product
    success_url = reverse_lazy('catalog:home')

