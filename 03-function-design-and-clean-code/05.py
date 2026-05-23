def register_user(data: dict) -> dict:
    
    validate_registration_data(data)
    normalized_data = normalize_registration_data(data)
    active_user_data = build_user(normalized_data)
    
    return active_user_data
    ...

# input must have:
# username
# email
# age
# ------------------------
# output is like:
# {
#     "username": "...",
#     "email": "...",
#     "age": 20,
#     "is_active": True,
# }
# ------------------------
# Normalization:
# username: trim و lowercase
# email: trim و lowercase


def validate_registration_data(data: dict) -> None:
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    if data["username"].strip() == "":
        raise ValueError("username is required")
    if not "@" in data["email"]:
        raise ValueError("email is invalid")
    if data["email"].strip() == "":
        raise ValueError("email is required")
    if not data["age"] >= 18:
        raise ValueError("age must be at least 18")

def normalize_registration_data(data: dict) -> dict:
    data["username"] = data["username"].strip().lower()
    data["email"] = data["email"].strip().lower()
    return data

def build_user(normalized_data: dict) -> dict:
    normalized_data["is_active"] = True
    return normalized_data

