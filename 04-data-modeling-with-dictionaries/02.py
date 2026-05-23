# def build_order_item_summaries(items: list[dict]) -> list[dict]:
        
#     order_item_summaries = [{"product_id": item["product_id"], "name": item["name"],"quantity": item["quantity"], "line_total": item["quantity"]*item["unit_price"] } for item in items]
        
#     return order_item_summaries

def build_order_item_summaries(items: list[dict]) -> list[dict]:
    return [
        {
            "product_id": item["product_id"],
            "name": item["name"],
            "quantity": item["quantity"],
            "line_total": item["unit_price"] * item["quantity"],
        }
        for item in items
    ]


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
