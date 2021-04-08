from products.models import Product
from inventories.models import Inventory
from products.serializers import ProductSerializer
from inventories.services import product_dict
from django.contrib.auth.models import User


def register_product(productData: dict, sellerId: int):

    # create product
    product = Product.objects.create(
        name=productData['name'],
        price=productData['price'],
        description=productData['description'],
        category=productData['category'],
        image=productData['image'],
    )

    seller = User.objects.get(id=sellerId)
    # create invetory

    inventory = Inventory.objects.create(
        total_amount=productData['amount'],
        product=product,
        seller=seller
    )

    inventory.available_product()
    inventory.product_data = product_dict(
        inventory.product)
    inventory.save()

    serializer = ProductSerializer(product).data

    return serializer
