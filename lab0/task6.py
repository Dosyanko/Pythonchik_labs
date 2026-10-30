def get_zodiac(date: str) -> str:

    parts = date.split(".")

    if len(parts) != 2:
        raise ValueError("Wrong date format")

    day = int(parts[0])
    month = int(parts[1])

    if (day > 31) or (day < 1):
        raise ValueError("There is no such day in month")
    if (month == 2) and (day > 29):
        raise ValueError("There is no such day in this month")

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    else:
        raise ValueError("Wrong date format")


if __name__ == "__main__":
    try:
        date = input("Enter your birth date (DD.MM): ")

        zodiac = get_zodiac(date)
    except (ValueError, EOFError) as e:
        print("Error: ", e)
    else:
        print(f"Output: {zodiac}. Do not use this as an answer to a security question!")
