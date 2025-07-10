def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_list = []
    for name, info in users.items():
        if info.get("active") is True:
            active_list.append(name)
    return active_list

# Test
users = {
    "Ali": {"active": True, "email": "ali@example.com"},
    "Vali": {"active": False, "email": "vali@example.com"},
    "Sami": {"active": True, "email": "sami@example.com"}
}
print(get_active_users(users))
