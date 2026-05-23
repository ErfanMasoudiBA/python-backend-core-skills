def calculate_shipping_cost(user: dict, cart_total: int) -> int:
    
    if not user["is_active"]:
        return -1
    
    if cart_total >= 500_000:
        return 0
    
    if user["city"] == "Tehran":
        return 30_000
    
    return 50_000
