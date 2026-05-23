def validate_cart_items(cart_items: list[dict]) -> None:
    if not isinstance(cart_items, list):
        raise TypeError("cart_items must be a list")

    if not cart_items:
        raise ValueError("cart_items must not be empty")

    seen_product_ids = set()

    for item in cart_items:
        if not isinstance(item, dict):
            raise TypeError("each cart item must be a dictionary")

        if "product_id" not in item:
            raise ValueError("product_id is required")
        if not isinstance(item["product_id"], int):
            raise TypeError("product_id must be an integer")

        if "quantity" not in item:
            raise ValueError("quantity is required")
        if not isinstance(item["quantity"], int):
            raise TypeError("quantity must be an integer")
        if item["quantity"] <= 0:
            raise ValueError("quantity must be greater than 0")

        if "unit_price" not in item:
            raise ValueError("unit_price is required")
        if not isinstance(item["unit_price"], int):
            raise TypeError("unit_price must be an integer")
        if item["unit_price"] <= 0:
            raise ValueError("unit_price must be greater than 0")

        if item["product_id"] in seen_product_ids:
            raise ValueError(f"duplicate product_id: {item['product_id']}")

        seen_product_ids.add(item["product_id"])



def calculate_total_quantity(cart_items: list[dict]) -> int:
    total_quantity = 0

    for cart_item in cart_items:
        total_quantity += cart_item["quantity"]

    return total_quantity


def calculate_total_price(cart_items: list[dict]) -> int:
    total_price = 0

    for cart_item in cart_items:
        total_price += cart_item["unit_price"] * cart_item["quantity"]

    return total_price


def build_cart_summary(cart_items: list[dict]) -> dict[str, int]:
    validate_cart_items(cart_items)

    return {
        "items_count": len(cart_items),
        "total_quantity": calculate_total_quantity(cart_items),
        "total_price": calculate_total_price(cart_items),
    }


test_cart_items = [
    {"product_id": 101, "quantity": 2, "unit_price": 50000},
    {"product_id": 205, "quantity": 1, "unit_price": 120000},
]
print(build_cart_summary(test_cart_items))