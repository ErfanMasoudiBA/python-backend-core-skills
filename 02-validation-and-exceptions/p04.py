def validate_cart_items(cart_items: list[dict]) ->None:
    if cart_items is None:
        raise ValueError("cart items must be filled.")
    
    if not isinstance(cart_items,list):
        raise TypeError("cart items must be a list.")
    
    seen_cart_items=set()
    
    for item in cart_items:
        if "product_id" not in item:
            raise ValueError("product id is required.")

        if not isinstance(item["product_id"], int):
            raise ValueError("product id must be an integer.")

        if "quantity" not in item:
            raise ValueError("quantity is required.")
    
        if not item["quantity"] >0:
            raise ValueError("quantity must be bigger than zero")
    
        if item["product_id"] in seen_cart_items:
            raise ValueError(f"product id {item['product_id']} is duplicated")
        seen_cart_items.add(item["product_id"])
    