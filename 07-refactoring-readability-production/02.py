# def calculate_discount(subtotal: int, is_premium: bool) -> int:
#     if is_premium:
#         return subtotal // 10
#     return 0


def calculate_discount(subtotal: int, is_premium: bool) -> int:
    if not is_premium:
        return 0
    return subtotal // 10
