from products.models import Product
from inventories.models import Inventory
from products.serializers import ProductSerializer

def register_product(productData):

    #create invetory
    inventory = Inventory.objects.create()


    product = Product.objects.create(
        name= productData['name'],
        price= productData['price'],
        description= productData['description'],
        inventory= inventory
    )

    serializer = ProductSerializer(product).data

    return serializer


