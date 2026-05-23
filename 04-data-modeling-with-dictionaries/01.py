def build_user_profile_summary(user: dict) -> dict:
    return {
        "id": user["id"],
        "username": user["username"],
        "city": user["address"]["city"],
        "is_active": user["is_active"]
    }


# input:
user = {
    "id": 1,
    "username": "ali",
    "email": "ali@example.com",
    "is_active": True,
    "address": {
        "city": "Tehran",
        "postal_code": "12345"
    }
}

print(build_user_profile_summary(user))

# output:
# {
#     "id": 1,
#     "username": "ali",
#     "city": "Tehran",
#     "is_active": True
# }
