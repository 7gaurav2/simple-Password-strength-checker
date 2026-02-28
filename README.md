# simple-Password-strength-checker
# Password Strength Checker (Python)

## Description

This project is a simple Password Strength Checker built using Python.  
It evaluates a user-entered password based on common security criteria and classifies it as Weak, Moderate, or Strong.

The goal of this project is to understand:
- Basic password security rules
- Regular expressions (regex)
- Input validation logic
- Structured function design in Python

---

## Features

The program checks whether a password:

- Has at least 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character

Based on the number of conditions satisfied:

- 0–2 checks → Weak
- 3–4 checks → Moderate
- 5 checks   → Strong

---

## Concepts Used

- Regular Expressions (re module)
- Boolean logic
- Function modularity
- Conditional statements
- Python dictionaries
- Program entry control using:

  if __name__ == "__main__":

---

## How It Works

1. The user enters a password.
2. Each validation function checks a specific security rule.
3. Results are stored in a dictionary.
4. The program counts how many rules passed.
5. A strength label is assigned.
6. Results are displayed clearly with PASS / FAIL indicators.

---

## Example Output

Enter a password to check: Admin123!

Check Results:
✅ PASS  —  Minimum 8 characters
✅ PASS  —  Contains uppercase letter
✅ PASS  —  Contains lowercase letter
✅ PASS  —  Contains a digit
✅ PASS  —  Contains special character

Passed : 5 / 5
Strength: Strong

---

## Limitations

- Does not check for dictionary words
- Does not check password reuse
- Does not measure entropy
- Does not detect common patterns (e.g., "123456", "password")

---

## Disclaimer

This project is for educational purposes only.
It demonstrates password strength validation logic and does not store or transmit passwords.

---

## Future Improvements

- Add entropy-based strength calculation
- Detect common weak passwords
- Add GUI interface
- Convert into a web-based password checker
