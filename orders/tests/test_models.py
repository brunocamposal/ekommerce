from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import Order
from inventories.models import Inventory
from products.models import Product


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create invetory model

        cls.seller = User.objects.create(
            username="admin",
            password="1234",
            is_superuser=True,
            is_staff=True
        )

        cls.product = Product.objects.create(
            name='product test',
            price=4.5,
            description='description test for product',
            image='image.png',
            category='categoria'
        )

        cls.inventory = Inventory.objects.create(
            total_amount=5,
            product=cls.product,
            seller=cls.seller
        )

        cls.order = Order.objects.create(
            total_price=1,
            comments="TEST",
            status="TEST",
            client_id=1
        )

    def test_create_order_fields(self):
        self.assertEqual(self.order.total_price, 1)
        self.assertEqual(self.order.id, 1)
        self.assertEqual(self.order.status, "TEST")
        self.assertEqual(self.order.client_id, 1)
