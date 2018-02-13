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
    items_per_page = 10
    page = 1

    def get_queryset(self):
        """ return books based on page """
        try:
            self.page = self.kwargs['page']
        except:
            self.page = 1

        return Book.objects.order_by('title')[self.page*self.items_per_page - self.items_per_page : self.page*self.items_per_page]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.page
        context['items_per_page'] = self.items_per_page

        return context


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

