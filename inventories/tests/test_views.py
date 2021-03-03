from rest_framework.test import APITestCase
from products.models import Product
from inventories.models import Inventory
from rest_framework.test import APIClient


class InventoryViewTest(APITestCase):
    def setUp(self):
        self.admin_data = {
            "username": "admin",
            "password": "1234",
            "is_superuser": True,
            "is_staff": True
        }

        self.admin_login_data = {
            "username": "admin",
            "password": "1234"
        }

        self.product_data_1 = {
            "name": "refrigerante Coca Cola",
            "price": 4.5,
            "description": "refrigerante Coca Cola garrafa 2 litros",
            "amount": 10
        }

        self.product_data_2 = {
            "name": "chocolate Laka",
            "price": 4.5,
            "description": "chocolate branco Laka",
            "amount": 0
        }

    def test_create_inventory(self):
        client = APIClient()

        # test with no products
        response = client.get(
            '/api/inventories/', format='json')

        self.assertEqual(response.status_code, 404)

        # create user
        client.post('/api/accounts/', self.admin_data, format='json')

        # login
        token = client.post(
            '/api/login/', self.admin_data, format='json').json()["token"]

        # validate token
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # create product
        client.post(
            "/api/products/", self.product_data_1, format='json').json()

        inventory = Inventory.objects.first()

        self.assertEqual(inventory.product_id.id, 1)
        self.assertEqual(inventory.product_id.name, "refrigerante Coca Cola")
        self.assertEqual(inventory.amount, 10)
        self.assertEqual(inventory.available, True)

    def test_create_inventory_with_no_quantity_in_inventory(self):
        client = APIClient()

        # create user
        client.post('/api/accounts/', self.admin_data, format='json')

        # login
        token = client.post(
            '/api/login/', self.admin_data, format='json').json()["token"]

        # validate token
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        client.post(
            "/api/products/", self.product_data_2, format='json').json()

        inventory = Inventory.objects.first()

        self.assertEqual(inventory.product_id.id, 1)
        self.assertEqual(inventory.product_id.name, "chocolate Laka")
        self.assertEqual(inventory.amount, 0)
        self.assertEqual(inventory.available, False)
