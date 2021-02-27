from django.test import TestCase
from products.models import Product, Inventory


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.invetory = Inventory.objects.create()