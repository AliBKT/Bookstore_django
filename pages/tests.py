from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class HomeTests(TestCase):

    def test_home_page_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_with_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_cantian(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')
