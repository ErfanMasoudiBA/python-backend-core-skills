def validate_username(username: str) -> None:
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    cleaned_username = username.strip()
    if cleaned_username.strip() == "":
        raise ValueError("Username is required.")

    if len(cleaned_username) < 3:
        raise ValueError("Username must be at least 3 characters long.")

    

validate_username("       شی")