def normalize_user_name(name: str) -> str:
    normalized_user_name = name.strip().title()
    return normalized_user_name

def normalize_user_email(email: str) -> str:
    normalized_user_email = email.strip().lower()
    return normalized_user_email

def validation_users(users: list[dict]) -> None:
    if not isinstance(users, list):
        raise TypeError("users must be a list")
    for user in users:
        if not isinstance(user, dict):
            raise TypeError("a user must be a dict") 

def normalize_users(users: list[dict]) -> list[dict]:
    validation_users(users)
    normalized_users = list()
    for user in users:
        normalized_users.append(
            {
                "id" : user["id"],
                "name" : normalize_user_name(user["name"]),
                "email" : normalize_user_email(user["email"])
            }
        )
        
    
    return normalized_users

# input
users = [
    {"id": 1, "name": "  ali  ", "email": "ALI@EXAMPLE.COM "},
    {"id": 2, "name": " sara", "email": " SARA@example.com"}
]
# output
# [
#     {"id": 1, "name": "Ali", "email": "ali@example.com"},
#     {"id": 2, "name": "Sara", "email": "sara@example.com"}
# ]

print(normalize_users(users))