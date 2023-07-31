def validate_password(password):
    if (len(password) < 8) or (' ' in password):
        return False
    upper = False
    lower = False
    digit = False
    #expected = False

    for char in password:
        if char.isupper():
            upper = True
            #expected = True
        elif char.islower():
            lower = True
            #expected = True
        elif char.isdigit():
            digit = True
            #expected = True
    if (upper == True) and (lower == True) and (digit == True):
        return True

    return False