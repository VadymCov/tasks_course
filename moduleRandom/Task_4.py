# 🔐 Password Generator 2
# This program generates n secure passwords, each m characters long.
# Each password includes lowercase and uppercase English letters and digits,
# excluding characters that are easily confused:
# 'l' (lowercase L), 'I' (uppercase i), '1' (digit one),
# 'o' and 'O' (lowercase and uppercase o), and '0' (zero).
#
# Additional requirement:
# Each password must contain at least:
# - one lowercase letter
# - one uppercase letter
# - one digit
#
# Input format:
# n — number of passwords to generate (integer)
# m — length of each password (integer)
#
# Output format:
# n lines, each containing a unique password of length m
#
# The solution is structured using two helper functions:
# - generate_password(length): returns a single valid password
# - generate_passwords(count, length): returns a list of count valid passwords


# Test ________________________________________________________________

from random import choice, choices
import string



def generate_password(length):
    upper_case = "".join(set(string.ascii_uppercase) - set("IO"))
    lower_case = "".join(set(string.ascii_lowercase) - set("lo"))
    digit_case = "".join(set(string.digits) - set("10"))

    all_chars = upper_case + lower_case + digit_case

    password = [
        choice(upper_case),
        choice(lower_case),
        choice(digit_case)
    ]
    password += choices(all_chars, k=length - 3)
    return "".join(password)

def generate_passwords(count, length):
    list_passwords = [generate_password(length) for _ in range(count)]
    passwords = "\n".join(list_passwords)
    return passwords

n, m = int(input()), int(input())

print(generate_passwords(n, m))