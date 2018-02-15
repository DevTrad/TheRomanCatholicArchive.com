from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Book, Category

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'recently_added_books'

    def get_queryset(self):
        """ return the most recently added books """
        return Book.objects.order_by('-id')[:5]


class CatalogView(generic.ListView):
    template_name = 'books/catalog.html'
    context_object_name = 'books'
    paginate_by = 10
    ordering = 'title'
    page = 1

    def get_queryset(self):
        """ Return list of books """
        category_id = self.request.GET.get('category')

        if category_id:
            return Book.objects.filter(categories=category_id)
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.request.GET.get('category')

        if category_id:
            context['category'] = Category.objects.get(id=category_id).name

        return context


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

def donate(request):
    render(request, 'books/donate.html')
