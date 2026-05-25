# # exercise 6
# def test_build_checkout_summary()->None:
#     # input
#     cart_items = [
#     {"name": "Laptop", "price": 1000, "quantity": 1},
#     {"name": "Mouse", "price": 100, "quantity": 2}
#     ]
#     # output
#     permium_summary = {
#         "items_count": 3,
#         "subtotal": 1200,
#         "discount": 120,
#         "shipping": 0,
#         "total": 1080
#     }
    
#     assert build_checkout_summary(cart_items,True) == permium_summary
    
    
#     non_permium_summary ={
#     "items_count": 3,
#     "subtotal": 1200,
#     "discount": 0,
#     "shipping": 0,
#     "total": 1200
#     }

#     assert build_checkout_summary(cart_items,False) == non_permium_summary

#     cart_items_02 = [
#     {"name": "Keyboard", "price": 300, "quantity": 2}
#     ]
#     assert calculate_subtotal(cart_items_02) == 600
    
#     assert calculate_discount(calculate_subtotal(cart_items_02), True) == 60
    
# # exercise 5
# def test_update_apply_discount_happy_path()-> None:

# products = [
# {"id": 1, "name": "Laptop", "price": 1000},
# {"id": 2, "name": "Mouse", "price": 100}
# ]


# applied_products = [
# {
#     "id": 1,
#     "name": "Laptop",
#     "original_price": 1000,
#     "discount_percent": 10,
#     "final_price": 900
# },
# {
#     "id": 2,
#     "name": "Mouse",
#     "original_price": 100,
#     "discount_percent": 10,
#     "final_price": 90
# }
# ]

# assert apply_discount(products, 10) == applied_products

# def test_update_apply_discount_no_mutation()->None:
#     products = [
#         {"id": 1, "name": "Laptop", "price": 1000},
#         {"id": 2, "name": "Mouse", "price": 100}
#     ]

#     original_products = [
#         {"id": 1, "name": "Laptop", "price": 1000},
#         {"id": 2, "name": "Mouse", "price": 100}
#     ]

#     result = apply_discount(products, 10)
#     # print(result) 
#     # print("--------")
#     # print(products)
#     # print("--------")
#     # print(original_products)

#     assert products == original_products


# test_update_apply_discount_no_mutation()
# test_update_apply_discount_happy_path()

# # exercise 4

# def test_update_order_status_invalid_status() -> None:
#     try:
#         update_order_status(order, "unknown")
#         assert False, "Expected ValueError"
#     except ValueError:
#         pass
    
#     try:
#         update_order_status(order, 123)
#         assert False, "Expected TypeError"
#     except TypeError:
#         pass


# order = {
#     "id": 101,
#     "status": "pending",
#     "paid": True
# }

# def test_update_order_status_no_mutation() -> None:
#     assert update_order_status(order,"paid") is not order
#     assert update_order_status(order,"shipped") is not order
#     assert update_order_status(order,"delivered") is not order
#     assert update_order_status(order,"cancelled") is not order

# test_update_order_status_no_mutation()
# test_update_order_status_invalid_status()


# # exercise 3

# order = {
#     "id": 101,
#     "status": "pending",
#     "paid": True
# }

# def test_update_order_status_no_mutation() -> None:
#     assert update_order_status(order,"paid") is not order
#     assert update_order_status(order,"shipped") is not order
#     assert update_order_status(order,"delivered") is not order
#     assert update_order_status(order,"cancelled") is not order

# test_update_order_status_no_mutation()

# # exercise 2

# def test_calculate_discount() -> None:
#     assert calculate_discount(1200, True) == 120
#     assert calculate_discount(12000, False) == 0
#     assert calculate_discount(999, True) == 99
#     assert calculate_discount(0, True) == 0

# test_calculate_discount()

# # exercise 1

# def test_calculate_shipping() -> None:
#     assert calculate_shipping(0) == 50 
#     assert calculate_shipping(999) == 50 
#     assert calculate_shipping(1000) == 0
#     assert calculate_shipping(1001) == 0

# test_calculate_shipping()
