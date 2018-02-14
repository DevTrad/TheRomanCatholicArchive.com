from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Book

class BookIndexViewTests(TestCase):
    """ Tests for books:index """

    def test_multiple_books(self):
        """
        The books index page can show the 5 most recent books (sorted by most recently added)
        """
        number_of_books = 10

        for i in range(1, number_of_books):
            Book.objects.create(
                title='Book ' + str(i), 
                author='Author' + str(i),
                publication_year=2000
            )

        response = self.client.get(reverse('books:index'))

        self.assertEqual(len(response.context['recently_added_books']), 5)


class BookCatalogViewTests(TestCase):
    """ Tests for books:catalog """
    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('books:catalog'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books found')
        self.assertQuerysetEqual(response.context['books'], [])

    def test_multiple_books(self):
        """
        The books catalog page can show multiple books (sorted alphabetically, paginated at 10 items per page)
        """
        number_of_books = 20
        books_list = []

        for i in range(1, number_of_books):
            Book.objects.create(
                title='Book ' + str(i), 
                author='Author' + str(i),
                publication_year=2000
            )

        response = self.client.get(reverse('books:catalog'))

        self.assertEqual(len(response.context['books']), 10)


class BookDetailViewTests(TestCase):
    """ Tests for books:detail """

    def test_existing_book(self):
        """
        If book exists, display details
        """
        book = Book.objects.create(title='A Book Title', author='Author McAuthorname', publication_year=2000)
        url = reverse('books:detail', args=(book.id,))

        response = self.client.get(url)

        self.assertContains(response, 'A Book Title')
        self.assertContains(response, 'Author McAuthorname')

    def test_non_existent_book(self):
        """
        If book does not exist return 404
        """
        response = self.client.get(reverse('books:detail', args=(1,)))

        self.assertEqual(response.status_code, 404)


