from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'recently_added_books'

    def get_queryset(self):
        """ return the most recently added books """
        return Book.objects.order_by('-id')[:5]


class CatalogView(generic.ListView):
    template_name = 'books/catalog.html'
    context_object_name = 'books'

    def get_queryset(self):
        """ return books based on page """
        return Book.objects.order_by('-id')


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

