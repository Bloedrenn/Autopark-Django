from datetime import date


def calculate_age(birthday):
    today = date.today()

    temp_age = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        temp_age -= 1

    age = temp_age

    return age
