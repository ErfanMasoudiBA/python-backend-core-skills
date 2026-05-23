# get_in_stock_product_ids(products)

# input
# products = [
#     {"id": 101, "name": "Keyboard", "in_stock": True},
#     {"id": 102, "name": "Mouse", "in_stock": False},
#     {"id": 103, "name": "Monitor", "in_stock": True},
# ]

# output
# [101, 103]



def get_in_stock_product_ids(products: list[dict]) -> list[int]:
    in_stock_product_ids  = list()
    
    for product in products:
        if product["in_stock"]: in_stock_product_ids .append(product["id"])
        
    return in_stock_product_ids 

test_input = [
    {"id": 101, "name": "Keyboard", "in_stock": True},
    {"id": 102, "name": "Mouse", "in_stock": False},
    {"id": 103, "name": "Monitor", "in_stock": True},
]
print(get_in_stock_product_ids(test_input))