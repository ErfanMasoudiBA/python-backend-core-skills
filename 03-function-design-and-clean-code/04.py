# def normalize_text(value: str) -> str:
#     if value.isdigit():
#         return value.strip()
#     return value.strip().lower()


# def build_user_contact_info(user: dict) -> dict:

#     return {
#         "email": normalize_text(user["email"]),
#         "phone": normalize_text(user["phone"]),
#         "username": normalize_text(user["username"]),
#     }



def normalize_text(value: str) -> str:
    return value.strip()

def normalize_identifier(value: str) -> str:
    return value.strip().lower()

def build_user_contact_info(user: dict) -> dict:
    return {
        "email": normalize_identifier(user["email"]),
        "phone": normalize_text(user["phone"]),
        "username": normalize_identifier(user["username"]),
    }
