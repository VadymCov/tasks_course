# 🔢 Operations on complex numbers
# Given two complex numbers. Write a program that calculates and outputs their sum, difference, and product.
# Input format: Two complex numbers are given to the program, each on a separate line.
# Output format: The program should output the answer to the task.


c_1 = complex(input())
c_2 = complex(input())
ad = f"{c_1} + {c_2} = {c_1 + c_2}"
sub= f"{c_1} - {c_2} = {c_1 - c_2}"
mul = f"{c_1} * {c_2} = {c_1 * c_2}"
print(ad, sub, mul, sep="\n")
