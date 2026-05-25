def build_checkout_summary(cart_items: list[dict], is_premium: bool) -> dict:
    validation_cart_items(cart_items, is_premium)
    
    items_count = get_items_count(cart_items)
    subtotal = calculate_subtotal(cart_items)
    discount = calculate_discount(subtotal,is_premium)
    shipping = calculate_shipping(subtotal)
    total = calculate_total(subtotal,discount, shipping)
    return {
    "items_count": items_count,
    "subtotal": subtotal,
    "discount": discount,
    "shipping": shipping,
    "total": total
}
