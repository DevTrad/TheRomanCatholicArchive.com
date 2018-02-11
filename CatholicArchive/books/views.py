from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'recently_added_books'

    def get_queryset(self):
        """ return the most recently added books """
        return Book.objects.order_by('-id')[:10]

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

