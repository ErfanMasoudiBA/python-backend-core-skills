def calculate_shipping(subtotal: int) -> int:
    if subtotal >= 1000:
        return 0
    return 50


def test_calculate_shipping() -> None:
    assert calculate_shipping(0) == 50 
    assert calculate_shipping(999) == 50 
    assert calculate_shipping(1000) == 0
    assert calculate_shipping(1001) == 0

test_calculate_shipping()