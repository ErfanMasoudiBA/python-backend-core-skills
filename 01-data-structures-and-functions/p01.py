# get_usernames(users)

# input
# users = [
#     {"id": 1, "username": "ali"},
#     {"id": 2, "username": "sara"},
#     {"id": 3, "username": "mamad"},
#     {"id": 4, "username": "ali"},
# ]

# output is the lists of our usernames
# ["ali", "sara", "mamad"]


def get_usernames(users: list[dict]) -> list[str]:
    usernames = list()
    
    for user in users: 
        usernames.append(user["username"])
        
    return usernames

input_test = [
    {"id": 1, "username": "ali"},
    {"id": 2, "username": "sara"},
    {"id": 3, "username": "mamad"},
]

print(get_usernames(input_test))