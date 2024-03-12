def validate_password(password):
    """
    Validates a password against common requirements:
    - Minimum length: 10 characters
    - Must contain at least one uppercase letter
    - Must contain at least one digit
    - Must contain at least one special character
    - Must contain the year 1999
    - Must contain leevste stadt dä Welt
    """
    requirements = [
        (len(password) >= 10, "Password must be at least 10 characters long"),

        (any(c.isupper() for c in password), "Password must contain at least one uppercase letter"),

        (any(c.isdigit() for c in password), "Password must contain at least one digit"),

        (any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for c in password), "Password must contain at least one special character"),

        ('1999' in password, "Password must contain the year founding year of mobile zone"),

        ('koeln' in password, "Password must contain leevste Stadt dä Welt")
    ]

    failed_requirements = [req[1] for req in requirements if not req[0]]

    return len(failed_requirements) == 0, failed_requirements

is_valid = False

while not is_valid:

    password = input("Enter a password: ")
    is_valid, failed_requirements = validate_password(password)


    if is_valid:
        print("Valid password!")
    else:
        print("Invalid password. Please try again.")

        print(failed_requirements[0])

        #alternativ und natürlich wesentlich benutzerfreundlicher
        #for requirement in failed_requirements:
           #print(requirement)
