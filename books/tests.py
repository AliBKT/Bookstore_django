from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from .models import Book


# Create your tests here.


class BookTests(TestCase):

    def setUp(self):
        self.model = get_user_model()
        self.model.objects.create_user(
            'UserTest',
            'example@gmail.com',
            "Asder\9874",
        )
        self.user = self.model.objects.last()
        Book.objects.create(title='test title', discription='test discription', author='test author', price=15,
                            user=self.user, cover='book/img.png')
        self.book = Book.objects.last()

    def test_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('book_deatail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_add_book_view_create_book(self):
        response = self.client.post(reverse('add_book'), {
             'title': 'test title',
             'discription': 'test discription',
             'author': 'test author',
             'price': 15,
             'user': self.user
         })
        self.assertEqual(response.status_code, 302)

    def test_add_book_view_template(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)