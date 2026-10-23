import random

code=random.randint(1,100)

while True:
    guess=input("Make your guess: ")

    if guess < code:
        print("Less")
    elif guess > code:
        print("Larger")
    else:
        print("Thats right")
        break