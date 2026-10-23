def is_palindrome(s):
    return s==s[::-1]

message=input("Enter your message: ")

if is_palindrome(message):
    print("Palindrome")
else:
    print("Not palindrome")
    