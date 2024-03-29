from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogRecord


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)

class BlogListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object



class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture', 'published_at', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:list')



