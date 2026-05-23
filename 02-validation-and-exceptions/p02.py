def validate_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if not age>0:
        raise ValueError("Age must be bigger than zero.")
    
validate_age(0)