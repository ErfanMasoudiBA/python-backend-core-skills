def build_discounted_product(product: dict, discount_percent: int) -> dict:
    final_price = calculate_final_price(product, discount_percent)

    return {
        "id": product["id"],
        "name": product["name"],
        "original_price": product["price"],
        "discount_percent": discount_percent,
        "final_price": final_price
    }


def apply_discount(products: list[dict], discount_percent: int) -> list[dict]:
    validation_inputs(products, discount_percent)

    discounted_products = []

    for product in products:
        discounted_product = build_discounted_product(product, discount_percent)
        discounted_products.append(discounted_product)

    return discounted_products
