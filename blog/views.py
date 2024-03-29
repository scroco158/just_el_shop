from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from blog.models import BlogRecord


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = BlogRecord


class BlogDetailView(DetailView):
    model = BlogRecord


class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture', 'published_at', 'is_published')
    success_url = reverse_lazy('blog:list')
