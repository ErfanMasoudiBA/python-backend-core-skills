def validation_products(products: list[dict])-> None:
    if not isinstance(products,list):
        raise TypeError("products is not list")
    for product in products:
        if not isinstance(product,dict):
            raise TypeError("a product is not dict")

def calculate_total_inventory_value(products: list[dict]) -> int:
    total_price = 0
    for product in products:
        total_price += product["stock"] * product["price"]
    return total_price

def calculate_total_stock(products: list[dict]) -> int:
    total_stock = 0
    for product in products:
        total_stock += product["stock"]
    return total_stock

def get_out_of_stocks(products: list[dict]) -> list:
    out_of_stocks = list()
    for product in products:
        if product["stock"] == 0:
            out_of_stocks.append(product["name"])
    return out_of_stocks

def build_inventory_report(products: list[dict]) -> dict:
    validation_products(products)
    return {
            "total_products": len(products),
            "total_stock": calculate_total_stock(products),
            "out_of_stock": get_out_of_stocks(products),
            "total_inventory_value": calculate_total_inventory_value(products)
        }

products = [
    {"name": "Laptop", "stock": 3, "price": 1000},
    {"name": "Mouse", "stock": 10, "price": 100},
    {"name": "Keyboard", "stock": 0, "price": 200}
]

print(build_inventory_report(products))

# {
#     "total_products": 3,
#     "total_stock": 13,
#     "out_of_stock": ["Keyboard"],
#     "total_inventory_value": 4000
# }
