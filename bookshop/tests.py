from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from bookshop.models import Author


class RegisterTest(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        response = self.client.post(
            reverse("bookshop:register-page"),
            data={
                "username": "alisher",
                "email": "muhitdnovm@gamil.com",
                "first_name": "Alisher",
                "last_name": "Sadullayev",
                "password1": "testpassword",
                "password2": "testpassword2",

            }
        )

    def test_user_password_wrong(self):
        response = self.client.post(
            reverse("bookshop:register-page"),
            data={
                "username": "alisher",
                "email": "muhitdnovm@gamil.com",
                "first_name": "Alisher",
                "last_name": "Sadullayev",
                "password1": "testpassword",
                "password2": "testpassword",

            }
        )
        count = Author.objects.count()

        self.assertEqual(count, 0)
