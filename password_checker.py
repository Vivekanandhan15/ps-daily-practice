password = input("Enter password: ")

special_chars = "!@#$%^&*"

if len(password) >= 8 and any(ch in special_chars for ch in password):
    print("Password is strong")
else:
    print("Password is not strong")
