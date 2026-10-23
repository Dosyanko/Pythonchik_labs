password=input("Enter your password: ")

if len(password) < 16:
    print("Too short")
elif password.isalpha() or password.isdigit():
    print("Weak password")
else:
    print("Strong password")    