import re

def evaluate_password_strength(password):
    # Initialize feedback and score
    feedback = []
    score = 0

    # Criteria checks
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\[\]\\|~`]', password)
    common_patterns = re.search(r'(password|1234|qwerty|admin)', password, re.IGNORECASE)

    # Scoring system
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
        
    if common_patterns:
        score -= 2

    # Generate feedback
    if length < 8:
        feedback.append("Password should be at least 8 characters long")
    if not has_upper:
        feedback.append("Add uppercase letters")
    if not has_lower:
        feedback.append("Add lowercase letters")
    if not has_digit:
        feedback.append("Add numbers")
    if not has_special:
        feedback.append("Add special characters (!@#$%^&* etc.)")
    if common_patterns:
        feedback.append("Avoid common words and patterns")

    # Determine strength level
    if score <= 2:
        strength = "Very Weak 🔴"
    elif score <= 4:
        strength = "Weak 🟠"
    elif score <= 6:
        strength = "Moderate 🟡"
    elif score <= 8:
        strength = "Strong 🟢"
    else:
        strength = "Very Strong 💪"

    return strength, feedback

def main():
    print("PROBEY INFOTECH Password Complexity Checker")
    print("-------------------------------------------")
    
    while True:
        password = input("\nEnter password (or 'q' to quit): ").strip()
        if password.lower() == 'q':
            break
            
        strength, feedback = evaluate_password_strength(password)
        
        print(f"\nStrength: {strength}")
        if feedback:
            print("Recommendations:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Excellent password! No recommendations needed.")

if __name__ == "__main__":
    main()