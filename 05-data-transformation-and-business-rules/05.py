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
    if is_premium:
        return subtotal // 10
    return 0

def calculate_shipping(subtotal: int) -> int:
    if subtotal >= 1000:
        return 0
    return 50

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
