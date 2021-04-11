from rest_framework.test import APITestCase
from orders.models import Order
from products.models import Product
from inventories.models import Inventory
from rest_framework.test import APIClient


class OrderViewTest(APITestCase):
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
            "category": "bebida",
            "image": "bebida.png",
            "price": 4.25,
            "description": "refrigerante Coca Cola garrafa 2 litros",
            "amount": 10
        }

        self.product_data_2 = {
            "name": "chocolate Laka",
            "category": "doce",
            "image": "chocolate.png",
            "price": 4.50,
            "description": "chocolate branco Laka",
            "amount": 10
        }

        self.order_data = {
            "product_list": [1, 2],
            "total_price": 8.75,
            "comments": "without tomato",
            "client_id": 1
        }

    def test_create_order(self):
        client = APIClient()

        # test with no products
        response = client.get(
            '/api/inventories/', format='json')

        self.assertEqual(response.status_code, 401)

        # create user
        client.post('/api/signup/', self.admin_data, format='json')

        # login
        token = client.post(
            '/api/login/', self.admin_data, format='json').json()["token"]

        # validate token
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # create product
        client.post(
            "/api/products/register/", self.product_data_1, format='json')

        client.post(
            "/api/products/register/", self.product_data_2, format='json')

        # create order
        client.post(
            "/api/orders/create_order/", self.order_data, format='json')

        order = Order.objects.first()

        self.assertEqual(order.id, 1)
        self.assertEqual(order.total_price, 8.75)
        self.assertEqual(order.status, 'REALIZADO')
        self.assertEqual(order.comments, 'without tomato')

    # def test_create_inventory_with_no_quantity_in_inventory(self):
    #     client = APIClient()

    #     # create user
    #     client.post('/api/accounts/', self.admin_data, format='json')

    #     # login
    #     token = client.post(
    #         '/api/login/', self.admin_data, format='json').json()["token"]

    #     # validate token
    #     client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    #     client.post(
    #         "/api/products/", self.product_data_2, format='json').json()

    #     inventory = Inventory.objects.first()

    #     self.assertEqual(inventory.product_id.id, 1)
    #     self.assertEqual(inventory.product_id.name, "chocolate Laka")
    #     self.assertEqual(inventory.amount, 0)
    #     self.assertEqual(inventory.available, False)
