from products.models import Product
from inventories.models import Inventory
from products.serializers import ProductSerializer
from django.utils import timezone


def register_product(productData):

    # create product
    product = Product.objects.create(
        name=productData['name'],
        price=productData['price'],
        description=productData['description'],
        category=productData['category'],
        image=productData['image'],
    )

    # create invetory
    inventory = Inventory.objects.create(
        amount=productData['amount'],
        transaction_time=timezone.now(),
        transaction_type='register',
        product_id=product,
    )

    inventory.available_product()
    inventory.save()

    serializer = ProductSerializer(product).data

    return serializer
