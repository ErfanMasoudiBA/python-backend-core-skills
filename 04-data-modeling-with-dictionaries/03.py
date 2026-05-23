def calculate_total_price (items: list[dict]) -> int:
    total_price  = 0
    for item in items:
        total_price  += item["unit_price"] * item["quantity"]
    return total_price 

def build_order_summary(order: dict) -> dict:
    return {
        "order_id": order["id"],
        "username": order["user"]["username"],
        "status": order["status"],
        "items_count": len(order["items"]),
        "total_price": calculate_total_price(order["items"])
    }

# input
order = {
    "id": 5001,
    "user": {
        "id": 1,
        "username": "ali"
    },
    "items": [
        {"product_id": 10, "name": "Keyboard", "unit_price": 700000, "quantity": 2},
        {"product_id": 12, "name": "Mouse", "unit_price": 300000, "quantity": 1},
    ],
    "status": "paid"
}

print(build_order_summary(order))


# output
# {
#     "order_id": 5001,
#     "username": "ali",
#     "status": "paid",
#     "items_count": 2,
#     "total_price": 1700000
# }
