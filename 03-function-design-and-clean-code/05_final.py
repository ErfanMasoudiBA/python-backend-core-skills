def validate_registration_data(data: dict) -> None:
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    required_fields = ["username", "email", "age"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is required")

    if not isinstance(data["username"], str):
        raise TypeError("username must be a string")
    if data["username"].strip() == "":
        raise ValueError("username cannot be empty")

    if not isinstance(data["email"], str):
        raise TypeError("email must be a string")
    if data["email"].strip() == "":
        raise ValueError("email cannot be empty")
    if "@" not in data["email"]:
        raise ValueError("email is invalid")

    if not isinstance(data["age"], int):
        raise TypeError("age must be an integer")
    if data["age"] < 18:
        raise ValueError("age must be at least 18")


def normalize_registration_data(data: dict) -> dict:
    return {
        "username": data["username"].strip().lower(),
        "email": data["email"].strip().lower(),
        "age": data["age"],
    }


def build_user(normalized_data: dict) -> dict:
    return {
        "username": normalized_data["username"],
        "email": normalized_data["email"],
        "age": normalized_data["age"],
        "is_active": True,
    }


def register_user(data: dict) -> dict:
    validate_registration_data(data)
    normalized_data = normalize_registration_data(data)
    return build_user(normalized_data)
