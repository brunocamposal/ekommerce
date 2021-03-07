from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class UserViewsTest(APITestCase):
    def setUp(self):
        self.user_admin = {
            "username": "admin",
            "password":  "admin@123",
            "is_superuser": True,
            "is_staff": True
        }

        self.user_admin_login = {
            "username": "admin",
            "password":  "admin@123"
        }

        self.user_salesman = {
            "username": "salesman",
            "password":  "salesman@456",
            "is_superuser": False,
            "is_staff": True
        }

        self.user_salesman_login = {
            "username": "salesman",
            "password":  "salesman@456"
        }

        self.user_client = {
            "username": "client",
            "password":  "client@789",
            "is_superuser": False,
            "is_staff": True
        }

        self.user_client_login = {
            "username": "client",
            "password":  "client@789"
        }

    def test_create_and_login_user_admin(self):
        client = APIClient()
        response = client.post('/api/signup/', self.user_admin, format='json')
        self.assertEqual(response.status_code, 201)

        login = client.login(**self.user_admin_login)
        client.logout()
        self.assertTrue(login)

    def test_create_and_login_user_salesman(self):
        client = APIClient()
        response = client.post(
            '/api/signup/', self.user_salesman, format='json')
        self.assertEqual(response.status_code, 201)

        login = client.login(**self.user_salesman_login)
        client.logout()
        self.assertTrue(login)

    def test_create_and_login_user_client(self):
        client = APIClient()
        response = client.post('/api/signup/', self.user_client, format='json')
        self.assertEqual(response.status_code, 201)

        login = client.login(**self.user_client_login)
        client.logout()
        self.assertTrue(login)
