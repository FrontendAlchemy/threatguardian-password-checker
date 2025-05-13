import re

def check_password_strength(password):
    common_passwords = {"password", "123456", "12345678", "qwerty", "abc123", "password1"}
    length_error = len(password) < 12
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    sequential_error = re.search(r"(012|123|234|abc|bcd|cde)", password.lower()) is not None
    common_error = password.lower() in common_passwords

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error, sequential_error, common_error]
    score = 7 - sum(errors)

    if score == 7:
        return "Very Strong 💪", "✅ This password is very strong and meets all security criteria."
    elif score >= 4:
        return "Moderate ⚠️", "⚠️ Your password is okay, but could be stronger."
    else:
        return "Weak ❌", "❌ Weak password. Use 12+ characters, mix of symbols, numbers, and avoid common patterns."
