import re

def check_length(password):
    """Password should be at least 8 characters long."""
    return len(password) >= 8

def check_uppercase(password):
    """Password should contain at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    """Password should contain at least one lowercase letter."""
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    """Password should contain at least one digit."""
    return bool(re.search(r'[0-9]', password))

def check_special_character(password):
    """Password should contain at least one special character."""
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def evaluate_password_strength(password):
    """
    Run all checks and return a strength rating:
    0-2 checks passed → Weak
    3-4 checks passed → Moderate
    5   checks passed → Strong
    """
    checks = {
        "Minimum 8 characters"       : check_length(password),
        "Contains uppercase letter"  : check_uppercase(password),
        "Contains lowercase letter"  : check_lowercase(password),
        "Contains a digit"           : check_digit(password),
        "Contains special character" : check_special_character(password),
    }

    passed_count = sum(checks.values())

    # Determine strength label based on number of passed checks
    if passed_count <= 2:
        strength_label = "Weak"
    elif passed_count <= 4:
        strength_label = "Moderate"
    else:
        strength_label = "Strong"

    return checks, passed_count, strength_label


def run_password_checker():
    """
    Main function to take user input and display password strength results.
    """
    print("=" * 40)
    print("      Password Strength Checker")
    print("=" * 40)

    user_password = input("Enter a password to check: ")

    check_results, passed_count, strength_label = evaluate_password_strength(user_password)

    print("\nCheck Results:")
    print("-" * 40)

    for check_name, is_passed in check_results.items():
        status = "✅ PASS" if is_passed else "❌ FAIL"
        print(f"  {status}  —  {check_name}")

    print("-" * 40)
    print(f"  Passed : {passed_count} / {len(check_results)}")
    print(f"  Strength: {strength_label}")
    print("=" * 40)

if __name__ == "__main__":
    run_password_checker()
    
