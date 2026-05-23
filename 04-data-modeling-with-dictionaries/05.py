def calculate_order_total(items: list[dict]) -> int:
    total_price = 0
    for item in items:
        total_price += item["unit_price"]* item["quantity"]
    return total_price

def calculate_customer_total_spent(orders: list[dict])-> int:
    total_spent = 0
    for order in orders:
        total_spent += calculate_order_total(order["items"])
    return total_spent

def build_customer_report(customer: dict) -> dict:
    return {
        "customer_id": customer["id"],
        "name": customer["name"],
        "is_active": customer["is_active"],
        "orders_count": len(customer["orders"]),
        "total_spent": calculate_customer_total_spent(customer["orders"])
    }

# input
customer = {
    "id": 1,
    "name": "Ali",
    "is_active": True,
    "orders": [
        {
            "id": 101,
            "items": [
                {"product_id": 1, "unit_price": 200000, "quantity": 2},
                {"product_id": 2, "unit_price": 50000, "quantity": 1},
            ]
        },
        {
            "id": 102,
            "items": [
                {"product_id": 3, "unit_price": 300000, "quantity": 1},
            ]
        }
    ]
}

print(build_customer_report(customer))

# output
# {
#     "customer_id": 1,
#     "name": "Ali",
#     "is_active": True,
#     "orders_count": 2,
#     "total_spent": 750000
# }

