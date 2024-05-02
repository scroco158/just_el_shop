from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category


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


class CategoryListView(ListView):
    model = Category


class ProductDetailView(LoginRequiredMixin, DetailView):  # ---_detail.html
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ver = Version.objects.filter(product=self.object)  # выборка всех версий текущего продукта
        v_pr = []
        current_v_pr = []
        for v in ver:
            if v.is_current:
                current_v_pr.append(v.name)
            v_pr.append(v.name)
            print(v.name)
        print(v_pr)
        context['v_pr'] = v_pr  # отправляю список версий продукта в шаблон
        context['current_v_pr'] = current_v_pr

        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):  # ---_form.html
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        # print('форм сет', formset.__dict__)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            # cur_ver = Version.objects.filter(product=self.object, is_current=True)
            # if len(cur_ver) > 1:
            #     raise ValueError('More than one version')
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        print(user)
        print(self.object.product_owner)
        if user == self.object.product_owner:
            return ProductForm
        if user.has_perm('catalog.can_publish_product') and user.has_perm('catalog.can_change_description') and user.has_perm('catalog.can_change_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):  # ---_form.html
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        product.product_owner = self.request.user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):  # ---_confirm_delete.html
    model = Product
    success_url = reverse_lazy('catalog:home')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')
