# model/password_model.py
import re

COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123", "111111",
    "123123", "123456789", "iloveyou", "admin"
}

SEQUENCE_PATTERNS = [
    "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "0123456789"
]

def has_sequence(password: str) -> bool:
    """Return True if password contains sequential chars of length 3+."""
    password_lower = password.lower()
    for seq in SEQUENCE_PATTERNS:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password_lower:
                return True
    return False

def has_repeated_chars(password: str) -> bool:
    """Return True if password has 3+ repeated characters in a row."""
    return bool(re.search(r"(.)\1\1", password))

def check_strength(password: str) -> dict:
    """
    Returns a dictionary:
    {
        "score": int (0-10),
        "strength": str ("Very Weak" - "Very Strong"),
        "feedback": str (suggestion to improve)
    }
    """
    score = 0
    feedback = []

    # Common passwords check
    if password.lower() in COMMON_PASSWORDS:
        return {"score": 0, "strength": "Very Weak", "feedback": "Avoid common passwords"}

    # Length
    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1
    else:
        feedback.append("Password too short (min 8 characters recommended)")

    # Character variety
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add digits")

    if any(not c.isalnum() for c in password):
        score += 2
    else:
        feedback.append("Add symbols (!@#$ etc.)")

    # Penalties
    if has_sequence(password):
        score -= 1
        feedback.append("Avoid sequences like '123' or 'abc'")

    if has_repeated_chars(password):
        score -= 1
        feedback.append("Avoid repeated characters like 'aaa' or '111'")

    # Clamp score between 0 and 10
    score = max(0, min(score, 10))

    # Determine strength label
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {"score": score, "strength": strength, "feedback": "; ".join(feedback)}

