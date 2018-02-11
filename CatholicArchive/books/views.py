from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    recently_added_books = Book.objects.order_by('-id')[:10]

    view_model = {
        'recently_added_books': recently_added_books
    }

    return render(request, 'books/index.html', view_model)


def detail(request):
    return HttpResponse('Detail view')
