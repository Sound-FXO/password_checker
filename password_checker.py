password = input("Введите пароль: ")
score = 0


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_symbols(password):
    symbols = "@#$%()&*"
    return any(symbol in symbols for symbol in password)


def is_very_long(password):
    return len(password) >= 12


def pass_rating():
    score = 0
    checkers_list = [
        has_upper_letters(password),
        has_lower_letters(password),
        has_digit(password),
        has_symbols(password),
        is_very_long(password),
    ]

    for checker in checkers_list:
        if checker is True:
            score += 2
    print(score)


if __name__ == "__main__":
    pass_rating()
