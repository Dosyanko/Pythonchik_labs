import random

code = random.randint(1, 100)

while True:
    guess = input("Make your guess: ")

    guess_int = int(guess)

    if guess_int < code:
        print("Less")
    elif guess_int > code:
        print("Larger")
    else:
        print("Thats right")
        break
