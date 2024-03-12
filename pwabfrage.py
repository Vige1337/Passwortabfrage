def validate_password(password):
    """
    Validates a password against common requirements:
    - Minimum length: 8 characters
    - Must contain at least one uppercase letter
    - Must contain at least one digit
    - Must contain at least one special character
    - Must contain the year 1999
    - Must contain 1FCKoeln
    """
    requirements = [
        (len(password) >= 16, "Password must be at least 16 characters long"),

        (any(c.isupper() for c in password), "Password must contain at least one uppercase letter"),

        (any(c.isdigit() for c in password), "Password must contain at least one digit"),

        (any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for c in password), "Password must contain at least one special character"),

        ('1999' in password, "Password must contain the year founding year of mobile zone"),

        ('1FCKoeln' in password, "Password must contain colognes most loved football club")
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
        for requirement in failed_requirements:
            print(requirement)
