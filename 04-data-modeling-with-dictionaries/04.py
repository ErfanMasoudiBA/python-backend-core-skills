def group_products_by_availability(products: list[dict]) -> dict:
    
    available_group = list()
    unavailable_group = list()
    
    for product in products:
        
        product_summary = {"id":product["id"], "name":product["name"]}
        
        if product["is_available"]:
            available_group.append(product_summary)
        else:
            unavailable_group.append(product_summary)
    
    return {
        "available": available_group,
        "unavailable": unavailable_group        
    }

# input
products = [
    {"id": 1, "name": "Laptop", "is_available": True},
    {"id": 2, "name": "Mouse", "is_available": False},
    {"id": 3, "name": "Keyboard", "is_available": True},
]

print(group_products_by_availability(products))

# output
# {
#     "available": [
#         {"id": 1, "name": "Laptop"},
#         {"id": 3, "name": "Keyboard"},
#     ],
#     "unavailable": [
#         {"id": 2, "name": "Mouse"},
#     ]
# }
