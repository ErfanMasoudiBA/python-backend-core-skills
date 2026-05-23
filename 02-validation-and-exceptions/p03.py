def validate_product_data(product: dict) -> None:
    if "id" not in product:
        raise ValueError("id is required!")
    if not isinstance(product["id"], int):
        raise TypeError("id must be an integer.")
    if "name" not in product:
        raise ValueError("name is required!")
    if product["name"].strip() == "":
        raise ValueError("name must be filled!")
    if "price" not in product:
        raise ValueError("price is required!")
    if not product["price"]>0:
        raise ValueError("price must be bigger than zero.")
    

test={
    "id" : 23,
    "name": "ali",
    "price": 5
}
validate_product_data(test)
print("test")