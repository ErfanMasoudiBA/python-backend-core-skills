
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
    
def update_order_status(order: dict, new_status: str) -> dict:
    validation_order_status(order, new_status)
    return {
        "id": order["id"],
        "status": new_status,
        "paid": order["paid"]
    }

def test_update_order_status_no_mutation() -> None:
    order = {
        "id": 101,
        "status": "pending",
        "paid": True
    }

    updated_order = update_order_status(order, "paid")

    assert updated_order is not order
    assert updated_order["status"] == "paid"
    assert order["status"] == "pending"

test_update_order_status_no_mutation()