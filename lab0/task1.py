user_input=input("Enter your full name: surname, first name, and patronymic ")

parts=user_input.split()

if len(parts) >=3:
    surname=parts[0].capitalize()
    first_name=parts[1][0].upper()
    patronymic=parts[2][0].upper()

    result = f"{surname} {first_name}.{patronymic}."

    print(f"Output: {result}")
else:
    print("More data is needed")    
