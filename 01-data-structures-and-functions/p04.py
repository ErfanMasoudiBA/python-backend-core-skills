# has_duplicate_product_ids(cart_items)

# cart_items = [
#     {"product_id": 101, "quantity": 2},
#     {"product_id": 205, "quantity": 1},
#     {"product_id": 101, "quantity": 3},
# ]

# True


def has_duplicate_product_ids(cart_items: list[dict]) -> bool:
    seen_product_ids = set()
    for cart_item in cart_items:
        if cart_item["product_id"] in seen_product_ids:
            return True
        seen_product_ids.add(cart_item["product_id"])
    return False


cart_items = [
    {"product_id": 101, "quantity": 2},
    {"product_id": 205, "quantity": 1},
    {"product_id": 101, "quantity": 3},
]

print(has_duplicate_product_ids(cart_items))