def calculate_total_price(products_list: list):
    total_price = 0
    for product in products_list:
        total_price += product.price

    return total_price
