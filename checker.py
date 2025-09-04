import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase, lowercase, numbers, special chars
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Feedback
    if strength <= 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Medium"
    else:
        remarks = "Strong"

    return remarks


# Test
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print("Password Strength:", check_password_strength(pwd))