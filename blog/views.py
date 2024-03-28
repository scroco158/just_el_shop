from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.models import BlogRecord


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture')
    success_url = reverse_lazy('catalog:home')

