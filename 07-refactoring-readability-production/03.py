def update_order_status(order: dict, new_status: str) -> dict:
    validation_order_status(order, new_status)

    # return {
    #     "id": order["id"],
    #     "status": new_status,
    #     "paid": order["paid"]
    # }
    
    return {**order, "status": new_status}

