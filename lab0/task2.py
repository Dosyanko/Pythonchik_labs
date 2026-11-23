def password_check(password: str) -> str:
    if len(password) < 16:
        return "Too short"
    elif password.isalpha() or password.isdigit():
        return "Weak password"
    else:
        return "Strong password"


if __name__ == "__main__":
    password = input("Enter your password: ")

    print(password_check(password))
