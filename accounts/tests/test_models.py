from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_admin = User.objects.create_user(
            username='admin',
            password='admin',
            is_superuser=True,
            is_staff=True
        )

        cls.user_client = User.objects.create_user(
            username='cient',
            password='client',
            is_superuser=False,
            is_staff=False
        )

        cls.user_salesman = User.objects.create_user(
            username='salesman',
            password='salesman',
            is_superuser=False,
            is_staff=True
        )

    def test_if_has_all_fields_filled_as_admin(self):
        self.assertIsInstance(self.user_admin.id, int)
        self.assertIsInstance(self.user_admin.username, str)
        self.assertIsInstance(self.user_admin.password, str)
        self.assertIsInstance(self.user_admin.is_superuser, bool)
        self.assertIsInstance(self.user_admin.is_staff, bool)

    def test_if_has_all_fields_filled_as_client(self):
        self.assertIsInstance(self.user_client.id, int)
        self.assertIsInstance(self.user_client.username, str)
        self.assertIsInstance(self.user_client.password, str)
        self.assertIsInstance(self.user_client.is_superuser, bool)
        self.assertIsInstance(self.user_client.is_staff, bool)

    def test_if_has_all_fields_filled_as_salesman(self):
        self.assertIsInstance(self.user_salesman.id, int)
        self.assertIsInstance(self.user_salesman.username, str)
        self.assertIsInstance(self.user_salesman.password, str)
        self.assertIsInstance(self.user_salesman.is_superuser, bool)
        self.assertIsInstance(self.user_salesman.is_staff, bool)

    def test_admin_permissions(self):
        self.assertTrue(self.user_admin.is_superuser)
        self.assertTrue(self.user_admin.is_staff)

    def test_client_permissions(self):
        self.assertFalse(self.user_client.is_superuser)
        self.assertFalse(self.user_client.is_staff)

    def test_salesman_permissions(self):
        self.assertFalse(self.user_salesman.is_superuser)
        self.assertTrue(self.user_salesman.is_staff)
