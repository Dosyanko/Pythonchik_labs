def standart_form(user_input: str) -> str:
    parts = user_input.split()

    if len(parts) >= 3:
        surname = parts[0].capitalize()
        first_name = parts[1][0].upper()
        patronymic = parts[2][0].upper()

        result = f"{surname} {first_name}.{patronymic}."

        return result
    else:
        raise ValueError("More data is needed.")


if __name__ == "__main__":
    try:
        user_input = input(
            "Enter your full name: surname, first name, and patronymic: "
        )

    except ValueError as e:
        print(e)
    else:
        print(standart_form(user_input))
