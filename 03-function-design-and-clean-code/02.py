def calculate_order_total(order: list[dict]) -> int:
    total_price = 0
    for item in order:
        total_price += item["unit_price"] * item["quantity"]
    return total_price

def calculate_discount(total_price:int) -> int:
    if total_price >= 1_000_000:
        return int(total_price * 0.1)
    return 0

def build_order_summary(order: dict) -> dict:
    
    total_price = calculate_order_total(order)
    total_discount = calculate_discount(total_price)
    final_price = total_price - total_discount

    return {
        "order_id": order["id"],
        "items_count": len(order["items"]),
        "total_price": total_price,
        "discount": total_discount,
        "final_price": final_price,
    }
