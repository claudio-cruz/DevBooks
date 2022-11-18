from django.shortcuts import render
from django.views import generic
from .models import Book


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(status='published').order_by('name')
    template_name = "finance.html"