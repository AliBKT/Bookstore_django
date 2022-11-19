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
        self.user = self.model.objects.first()

        self.model = get_user_model()
        self.model.objects.create_user(
            'UserTest2',
            'example2@gmail.com',
            "Asder\98747",
        )
        self.user2 = self.model.objects.last()

        Book.objects.create(title='test title', discription='test discription', author='test author', price=15,
                            user=self.user2, cover='')
        self.book_without_cover = Book.objects.first()

        Book.objects.create(title='test title', discription='test discription', author='test author', price=15,
                            user=self.user, cover='media/test.png')
        self.book_with_cover = Book.objects.last()

    def test_detail_view_without_cover(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('book_deatail', args=[self.book_without_cover.id]))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_with_cover(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('book_deatail', args=[self.book_with_cover.id]))
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

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_contain_book(self):
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'test discription')

    def test_book_list_url(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_delete_book_view_name(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete_book', args=[self.book_with_cover.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_book_view_can_delete_book(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete_book', args=[self.book_with_cover.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_book_view_can_delete_book_with_other_user(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete_book', args=[self.book_without_cover.id]))
        self.assertEqual(response.status_code, 403)

    def test_update_book_view_can_update(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('update_book', args=[self.book_with_cover.id]), {
            'title': 'test title',
            'discription': 'test discription1',
            'author': 'test author',
            'price': 15,
        })
        self.assertEqual(response.status_code, 302)

    def test_update_book_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('update_book', args=[self.book_with_cover.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_book_view_can_update_with_other_user(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('update_book', args=[self.book_without_cover.id]), {
            'title': 'test title',
            'discription': 'test discription4',
            'author': 'test author',
            'price': 15,
        })
        self.assertEqual(response.status_code, 403)
