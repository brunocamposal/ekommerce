from django.test import TestCase
from products.models import Product
from inventories.models import Inventory


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create invetory model

        cls.product = Product.objects.create(
            name= 'product test',
            price= 4.5,
            description= 'description test for product',
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.product.name,  str)
        self.assertIsInstance(self.product.price,  float)
        self.assertIsInstance(self.product.description,  str)
        self.assertIsInstance(self.product.image, str)
        self.assertIsInstance(self.product.category, str)

    def test_amount_property(self):

        amount_result = self.product.amount()
        amount_expected = 5
        self.assertEquals(amount_result, amount_expected)
