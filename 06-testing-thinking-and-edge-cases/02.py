def calculate_discount(subtotal: int, is_premium: bool) -> int:
    if is_premium:
        return subtotal // 10
    return 0

def test_calculate_discount() -> None:
    assert calculate_discount(1200, True) == 120
    assert calculate_discount(12000, False) == 0
    assert calculate_discount(999, True) == 99
    assert calculate_discount(0, True) == 0

test_calculate_discount()