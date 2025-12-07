def check_strength(password: str) -> str:
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 1:
        return "Very Weak"
    if score == 2:
        return "Weak"
    if score == 3:
        return "Medium"
    if score == 4:
        return "Strong"
    return "Very Strong"
