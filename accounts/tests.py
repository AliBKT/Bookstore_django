from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.


class SignUpPageTest(TestCase):

    def test_signup_url_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_name_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_template_page(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_registration_request(self):
        response = self.client.post(reverse('signup'), {
            'username': 'UserTest',
            'email': 'example@gmail.com',
            'first_name': 'foo',
            'last_name': 'foo_lastname',
            'age': 12,
            'password1': "Asder\9874",
            'password2': "Asder\9874",
        })
        self.assertEqual(response.status_code, 302)

    def test_login_request(self):
        model = get_user_model()
        model.objects.create_user(
            'UserTest',
            'example@gmail.com',
            "Asder\9874",
        )
        response = self.client.post(reverse('login'), {
            'username': "UserTest",
            'password': "Asder\9874"
        })
        self.assertEqual(response.status_code, 302)
