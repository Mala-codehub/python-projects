import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return False, ["Password should be at least 8 characters long."]
    
    feedback = []

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if not re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/\\~`|\"']", password):
        feedback.append("Password should contain at least one special character.")

    return len(feedback) == 0, feedback

def main():
    password = input("Enter your password: ")
    is_strong, feedback = check_password_strength(password)
    
    if is_strong:
        print("Your password is strong!")
    else:
        print("Your password is weak:")
        for message in feedback:
            print("-", message)

if __name__ == "__main__":
    main()