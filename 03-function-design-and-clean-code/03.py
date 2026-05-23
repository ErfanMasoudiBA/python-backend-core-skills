def is_premium_user(user: dict) -> bool:
    if not user["is_active"]:
        return False

    if not user["email_verified"]:
        return False

    if user["orders_count"] < 10:
        return False

    return True



def get_premium_usernames(users: list[dict]) -> list[str]:
    result = []
    
    for user in users:
        if is_premium_user(user):
            result.append(user["username"])

    return result
