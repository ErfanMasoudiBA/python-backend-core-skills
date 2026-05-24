# Exercise 1
def validation_inputs(products: list[dict], discount_percent: int) -> None:
    
    if discount_percent<0 or discount_percent>100 :
        raise ValueError("The discount must between 0 and 100.")
    if not isinstance(products,list):
        raise TypeError("products is not a list.")
    for product in products:
        if not isinstance(product,dict):
            raise TypeError("each item in products list must be a dictionary")
        if not isinstance(product["price"],int):
                raise TypeError("price is not an integer.")
        if not product["price"]> 0:
            raise TypeError("price is not a positive integer.")

def calculate_final_price(product: dict, discount_percent: int) -> int:
    return product["price"] - (product["price"] * discount_percent / 100)

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

...

# Exercise 2

def update_order_status(order: dict, new_status: str) -> dict:
    validation_order_status(order,new_status)
    updated_order_status = order
    updated_order_status["status"] = new_status
    return updated_order_status

# these are allowed:
# "pending"
# "paid"
# "shipped"
# "delivered"
# "cancelled"

valid_status=["pending", "paid","shipped","delivered","cancelled"]

def validation_order_status(order: dict, new_status: str)-> None:
    if not isinstance(order, dict):
        raise TypeError("order is not a dict")
    if not order["status"] in valid_status:
        raise ValueError("Invalid status")
    if not new_status in valid_status:
        raise ValueError("Invalid status")
    if order["paid"] == False and new_status == "shipped":
        raise ValueError("has not paid yet")
    if order["status"] == "cancelled" or order["status"] == "delivered":
        raise ValueError("delivered or cancelled statuses can not change")
    

# input
order = {
    "id": 101,
    "status": "pending",
    "paid": True
}


print(update_order_status(order, "paid"))
print(update_order_status(order, "shipped"))
print(update_order_status(order, "delivered"))
# print(update_order_status(order, "cancelled"))
...

# Exercise 3

def normalize_user_name(name: str) -> str:
    normalized_user_name = name.strip().title()
    return normalized_user_name

def normalize_user_email(email: str) -> str:
    normalized_user_email = email.strip().lower()
    return normalized_user_email

def validation_users(users: list[dict]) -> None:
    if not isinstance(users, list):
        raise TypeError("users must be a list")
    for user in users:
        if not isinstance(user, dict):
            raise TypeError("a user must be a dict") 
    
    pass

def normalize_users(users: list[dict]) -> list[dict]:
    validation_users(users)
    normalized_users = list()
    for user in users:
        normalized_users.append(
            {
                "id" : user["id"],
                "name" : normalize_user_name(user["name"]),
                "email" : normalize_user_email(user["email"])
            }
        )
        
    
    return normalized_users

# input
users = [
    {"id": 1, "name": "  ali  ", "email": "ALI@EXAMPLE.COM "},
    {"id": 2, "name": " sara", "email": " SARA@example.com"}
]
# output
# [
#     {"id": 1, "name": "Ali", "email": "ali@example.com"},
#     {"id": 2, "name": "Sara", "email": "sara@example.com"}
# ]

print(normalize_users(users))
...

# Exercise 4

def validation_products(products: list[dict])-> None:
    if not isinstance(products,list):
        raise TypeError("products is not list")
    for product in products:
        if not isinstance(product,dict):
            raise TypeError("a product is not dict")

def calculate_total_price(products: list[dict]) -> int:
    total_price = 0
    for product in products:
        total_price += product["stock"] * product["price"]
    return total_price

def calculate_total_stock(products: list[dict]) -> int:
    total_stock = 0
    for product in products:
        total_stock += product["stock"]
    return total_stock

def get_out_of_stocks(products: list[dict]) -> list:
    out_of_stocks = list()
    for product in products:
        if product["stock"] == 0:
            out_of_stocks.append(product["name"])
    return out_of_stocks

def build_inventory_report(products: list[dict]) -> dict:
    validation_products(products)
    return {
            "total_products": len(products),
            "total_stock": calculate_total_stock(products),
            "out_of_stock": get_out_of_stocks(products),
            "total_inventory_value": calculate_total_price(products)
        }

products = [
    {"name": "Laptop", "stock": 3, "price": 1000},
    {"name": "Mouse", "stock": 10, "price": 100},
    {"name": "Keyboard", "stock": 0, "price": 200}
]

print(build_inventory_report(products))

# {
#     "total_products": 3,
#     "total_stock": 13,
#     "out_of_stock": ["Keyboard"],
#     "total_inventory_value": 4000
# }

...

# Exercise 5

def get_items_count(cart_items: list[dict]) -> int:
    items_count = 0
    for item in cart_items:
        items_count += item["quantity"]
    return items_count

def calculate_subtotal(cart_items: list[dict]) -> int:
    subtotal = 0
    for item in cart_items:
        subtotal += item["price"]* item["quantity"]
    return subtotal

def calculate_discount(subtotal: int,is_premium: bool) -> int:
    discount = 0
    if is_premium:
        discount = subtotal / 10
    return discount

def calculate_shipping(subtotal: int) -> int:
    shipping = 50
    if subtotal >= 1000:
        shipping = 0
    return shipping

def calculate_total(subtotal: int ,discount: int, shipping:int)-> int:
    return subtotal - discount + shipping

def validation_cart_items(cart_items: list[dict], is_premium: bool)-> None:
    if not isinstance(cart_items, list):
        raise TypeError("cart items are not list")
    for item in cart_items:
        if not isinstance(item, dict):
            raise TypeError("a cart item is not dict")
    if not isinstance(is_premium, bool):
        raise TypeError("is_premium is not bool")

def build_checkout_summary(cart_items: list[dict], is_premium: bool) -> dict:
    validation_cart_items(cart_items, is_premium)
    subtotal = calculate_subtotal(cart_items)
    discount = calculate_discount(subtotal,is_premium)
    shipping = calculate_shipping(subtotal)
    return {
    "items_count": get_items_count(cart_items),
    "subtotal": subtotal,
    "discount": discount,
    "shipping": shipping,
    "total": calculate_total(subtotal,discount, shipping)
}




# input
cart_items = [
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 100, "quantity": 2}
]

print(build_checkout_summary(cart_items,True))


# output
# {
#     "items_count": 3,
#     "subtotal": 1200,
#     "discount": 120,
#     "shipping": 0,
#     "total": 1080
# }

...
