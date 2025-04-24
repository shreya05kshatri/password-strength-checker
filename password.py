# Step 1: Check password 
def check_password_criteria(password):
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in r"!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)

    return length, has_upper, has_lower, has_digit, has_special

# Step 2: password strength
def evaluate_strength(criteria):
    score = sum(criteria)
    if score == 5:
        return "Strong"
    elif score >= 3 and criteria[0]:
        return "Moderate"
    else:
        return "Weak"

# Step 3: feedback messages
def give_feedback(criteria):
    feedback = []
    labels = [
        "at least 8 characters",
        "an uppercase letter",
        "a lowercase letter",
        "a digit",
        "a special character"
    ]
    
    for check, message in zip(criteria, labels):
        if not check:
            feedback.append(f" Add {message}")
    
    return feedback

# Step 4: user for input and show result
password = input("Enter your password: ")

criteria = check_password_criteria(password)
strength = evaluate_strength(criteria)
feedback = give_feedback(criteria)

print(f"\nPassword Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for item in feedback:
        print(" -", item)
else:
    print("Password is strong!")
