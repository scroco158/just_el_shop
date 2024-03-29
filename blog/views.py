from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from blog.models import BlogRecord


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = BlogRecord


