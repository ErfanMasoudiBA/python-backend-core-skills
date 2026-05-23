# calculate_total_quantity(cart_items)

# input
# cart_items = [
#     {"product_id": 101, "quantity": 2},
#     {"product_id": 205, "quantity": 1},
#     {"product_id": 309, "quantity": 4},
# ]


# output
# 7

def calculate_total_quantity(cart_items:list[dict])-> int:
    num_cart_items = 0
    for cart_item in cart_items:
        num_cart_items += cart_item["quantity"]
    return num_cart_items

test_cart_items = [
    {"product_id": 101, "quantity": 2},
    {"product_id": 205, "quantity": 1},
    {"product_id": 309, "quantity": 4},
]

print(calculate_total_quantity(test_cart_items))