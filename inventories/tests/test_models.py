from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product
from ..models import Inventory, InventoryRecords


class IventoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create seller
        cls.seller = User.objects.create(
            username="admin",
            password="1234",
            is_superuser=True,
            is_staff=True
        )
        # create product
        cls.product = Product.objects.create(
            name='product test',
            price=4.5,
            description='description test for product'
        )
        # create inventory
        cls.inventory = Inventory.objects.create(
            total_amount=15,
            available=True,
            product=cls.product,
            seller=cls.seller
        )

        # create inventory records
        cls.inventory_records = InventoryRecords.objects.create(
            amount=10,
            transaction_type="refuel",
            transaction_time=timezone.now(),
            product=cls.product,
            seller=cls.seller
        )

    def test_create_inventory_model(self):
        self.assertEqual(self.inventory.id, 1)
        self.assertEqual(self.inventory.total_amount, 15)
        self.assertEqual(self.inventory.available, True)
        self.assertIsInstance(self.inventory.product, Product)
        self.assertIsInstance(self.inventory.seller, User)

    def test_create_inventory_records_model(self):
        self.assertEqual(self.inventory_records.id, 1)
        self.assertEqual(self.inventory_records.amount, 10)
        self.assertEqual(self.inventory_records.transaction_type, "refuel")
        self.assertIsInstance(self.inventory_records.product, Product)
        self.assertIsInstance(self.inventory_records.seller, User)
