from products.models import Product
from inventories.models import Inventory
from products.serializers import ProductSerializer


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
        total_amount=productData['amount'],
        product=product,
    )

    inventory.available_product()
    inventory.save()

    serializer = ProductSerializer(product).data

    return serializer
