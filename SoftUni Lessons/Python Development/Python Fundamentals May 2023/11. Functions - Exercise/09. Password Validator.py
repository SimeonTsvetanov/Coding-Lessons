def password_validator(password):
    result = ''
    valid = True

    if not (6 <= len(password) <= 10):
        result += f"Password must be between 6 and 10 characters\n"
        valid = False
    if not password.isalnum():
        result += f"Password must consist only of letters and digits\n"
        valid = False
    if len([i for i in password if i.isdigit()]) < 2:
        result += f"Password must have at least 2 digits\n"
        valid = False

    if valid:
        return f"Password is valid"
    else:
        return result


print(password_validator(input()))
