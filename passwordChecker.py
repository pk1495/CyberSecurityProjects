import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc.)")

    return score, feedback

#Run code
user_password = input("Enter a password to check: ")
score, tips = check_password_strength(user_password)

print("\nPassword Score:", str(score) + "/4")

if score == 4:
    print("✅ Strong password!")
else:
    print("⚠️  Weak password. Suggestions:")
    for tip in tips:
        print(" -", tip)
