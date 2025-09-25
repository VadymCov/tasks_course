# 🔐 Password Generator 1
# Write a program that uses the `random` module to generate n passwords of length m characters, consisting of lowercase and uppercase English letters and digits, except for those that are easily confused with each other:
# "l" (lowercase L);
# "I" (uppercase i);
# "1" (digit);
# "o" and "O" (lowercase and uppercase letters);
# "0" (digit).
# 
# Input Format: The program receives two numbers n and m, each on a separate line.
# Output Format: The program should output n passwords of length m characters according to the task conditions, each on a separate line.
# 
# Note 1: Consider that the numbers n and m are always such that generating the required passwords is possible.
# Note 2: Each password does not necessarily have to contain at least one digit and letter in upper and lower case.
# Note 3: It's convenient to structure the solution using two helper functions:
# generate_password(length) function – returns a random password of length characters;
# generate_passwords(count, length) function – returns a list consisting of count random passwords of length characters.


# Test __________________________________________________________________

import random
import string

def generate_password(length):
    product = [i for i in string.ascii_letters + string.digits if i not in ("0lI1oO")]
    password = "".join(random.sample(product, length))
    return password

def generate_passwords(count, length):
    list_password= [generate_password(length) for _ in range(count)]
    return list_password    

n, m = int(input()), int(input())
print(*generate_passwords(n,m), sep="\n")
