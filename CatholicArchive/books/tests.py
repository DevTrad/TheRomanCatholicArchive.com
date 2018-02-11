from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Book

class BookIndexViewTests(TestCase):
    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('books:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books found')
        self.assertQuerysetEqual(response.context['recently_added_books'], [])

    def test_multiple_books(self):
        """
        The books index page can show multiple books (sorted by most recently added)
        """
        number_of_books = 10

        for i in range(1, number_of_books):
            Book.objects.create(
                title='Book ' + str(i), 
                author='Author' + str(i),
                publication_date=timezone.now()
            )

        response = self.client.get(reverse('books:index'))

        self.assertQuerysetEqual(
            response.context['recently_added_books'],
            [('<Book: Book ' + str(n) + '>') for n in range(number_of_books - 1, 0, -1)]
        )


class BookDetailViewTests(TestCase):
    def test_existing_book(self):
        """
        If book exists, display details
        """
        book = Book.objects.create(title='A Book Title', author='Author McAuthorname', publication_date=timezone.now())
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
