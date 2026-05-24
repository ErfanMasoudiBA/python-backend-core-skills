def validation_inputs(products: list[dict], discount_percent: int) -> None:
    if not isinstance(products, list):
        raise TypeError("products must be a list.")

    if not isinstance(discount_percent, int):
        raise TypeError("discount_percent must be an integer.")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100.")

    for product in products:
        if not isinstance(product, dict):
            raise TypeError("each item in products list must be a dictionary.")

        if not isinstance(product["price"], int):
            raise TypeError("price must be an integer.")

        if product["price"] <= 0:
            raise ValueError("price must be positive.")


def calculate_final_price(product: dict, discount_percent: int) -> int:
    return product["price"] - (product["price"] * discount_percent // 100)

def apply_discount(products: list[dict], discount_percent: int) -> list[dict]:
    validation_inputs(products,discount_percent)
    
    products_applied_discount = list()
    for product in products:
        final_price = calculate_final_price(product,discount_percent)
        products_applied_discount.append({
                "id": product["id"], 
                "name": product["name"],
                "original_price": product["price"],
                "discount_percent": discount_percent,
                "final_price": final_price
            }
        )


    
    return products_applied_discount


# input
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Mouse", "price": 100}
]
print(apply_discount(products, 10))

# output
# [{
#     "id": 1,
#     "name": "Laptop",
#     "original_price": 1000,
#     "discount_percent": 10,
#     "final_price": 900
# },
# {
#     "id": 2,
#     "name": "Mouse",
#     "original_price": 100,
#     "discount_percent": 10,
#     "final_price": 90
# }]
