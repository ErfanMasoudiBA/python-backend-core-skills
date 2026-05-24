def update_order_status(order: dict, new_status: str) -> dict:
    validation_order_status(order, new_status)

    return {
        "id": order["id"],
        "status": new_status,
        "paid": order["paid"]
    }


# these are allowed:
# "pending"
# "paid"
# "shipped"
# "delivered"
# "cancelled"

valid_status=["pending", "paid","shipped","delivered","cancelled"]

def validation_order_status(order: dict, new_status: str)-> None:
    if not isinstance(new_status, str):
        raise TypeError("new_status must be a string.")
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
print(update_order_status(order, "cancelled"))