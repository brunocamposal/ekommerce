from products.models import Product
from .product_dict import product_dict


def inventories_list_dict(inventory_list) -> dict:

    for inventory in inventory_list:
        inventory.product_data = product_dict(inventory.product)
    
    return inventory_list
