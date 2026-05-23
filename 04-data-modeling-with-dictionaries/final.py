# Exercise 1

def build_user_profile_summary(user: dict) -> dict:
    return {
        "id": user["id"],
        "username": user["username"],
        "city": user["address"]["city"],
        "is_active": user["is_active"]
    }


# input:
user = {
    "id": 1,
    "username": "ali",
    "email": "ali@example.com",
    "is_active": True,
    "address": {
        "city": "Tehran",
        "postal_code": "12345"
    }
}

print(build_user_profile_summary(user))

# output:
# {
#     "id": 1,
#     "username": "ali",
#     "city": "Tehran",
#     "is_active": True
# }

...

# Exercise 2

def build_order_item_summaries(items: list[dict]) -> list[dict]:
        
    order_item_summaries = [{"product_id": item["product_id"], "name": item["name"],"quantity": item["quantity"], "line_total": item["quantity"]*item["unit_price"] } for item in items]
        
    return order_item_summaries

# input
items = [
    {"product_id": 10, "name": "Keyboard", "unit_price": 700000, "quantity": 2},
    {"product_id": 12, "name": "Mouse", "unit_price": 300000, "quantity": 1},
]

print(build_order_item_summaries(items))


# output
# [
#     {
#         "product_id": 10,
#         "name": "Keyboard",
#         "quantity": 2,
#         "line_total": 1400000,
#     },
#     {
#         "product_id": 12,
#         "name": "Mouse",
#         "quantity": 1,
#         "line_total": 300000,
#     }
# ]

...

# Exercise 3

def calculate_order_total_price(items: list[dict]) -> int:
    order_total_price = 0
    for item in items:
        order_total_price += item["unit_price"] * item["quantity"]
    return order_total_price

def build_order_summary(order: dict) -> dict:
    order_summary = dict()
    order_summary = {
        "id": order["id"],
        "username": order["user"]["username"],
        "status": order["status"],
        "items_count": len(order["items"]),
        "total_price": calculate_order_total_price(order["items"])
    }
    return order_summary

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

...

# Exercise 4

def group_products_by_availability(products: list[dict]) -> dict:
    
    available_group = list()
    unavailable_group = list()
    
    for product in products:
        if product["is_available"] == True:
            available_group.append({"id":product["id"], "name":product["name"]})
        else:
            unavailable_group.append({"id":product["id"], "name":product["name"]})
    
    return {
        "available": available_group,
        "unavailable": unavailable_group        
    }

# input
products = [
    {"id": 1, "name": "Laptop", "is_available": True},
    {"id": 2, "name": "Mouse", "is_available": False},
    {"id": 3, "name": "Keyboard", "is_available": True},
]

print(group_products_by_availability(products))

# output
# {
#     "available": [
#         {"id": 1, "name": "Laptop"},
#         {"id": 3, "name": "Keyboard"},
#     ],
#     "unavailable": [
#         {"id": 2, "name": "Mouse"},
#     ]
# }

...

# Exercise 5

def calculate_customer_an_order_spent(items: dict) -> int:
    total_price = 0
    for item in items:
        total_price += item["unit_price"]* item["quantity"]
    return total_price

def calculate_customer_total_spent(orders: list[dict])-> int:
    total_spent = 0
    for order in orders:
        total_spent += calculate_customer_an_order_spent(order["items"])
        pass
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


...
