
# build_cart_summary(cart_items)

# cart_items = [
#     {"product_id": 101, "quantity": 2, "unit_price": 50000},
#     {"product_id": 205, "quantity": 1, "unit_price": 120000},
# ]

# {
#     "items_count": 2,
#     "total_quantity": 3,
#     "total_price": 220000,
# }

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

def build_cart_summary(cart_items: list[dict]) -> dict:
    
    items_count = len(cart_items)
    total_quantity = calculate_total_quantity(cart_items)
    total_price = calculate_total_price(cart_items)
    
    cart_summary = {
        "items_count": items_count,
        "total_quantity": total_quantity,
        "total_price": total_price,
    }
    return cart_summary

test_cart_items = [
    {"product_id": 101, "quantity": 2, "unit_price": 50000},
    {"product_id": 205, "quantity": 1, "unit_price": 120000},
]

print(build_cart_summary(test_cart_items))