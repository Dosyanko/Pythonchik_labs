def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    message = input("Enter your message: ")

    if is_palindrome(message):
        print("Palindrome")
    else:
        print("Not palindrome")
