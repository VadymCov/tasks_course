# 🔢 Conjugate numbers
# Given a natural number n and two complex numbers z1, z2. Write a program that computes and outputs the value of the expression:
# sqrt(z1**n + z2**n + conj(z1)**n + conj(z2)**n + 1) / (z1**n + z2**n + conj(z1)**n + conj(z2)**n + 1)
# Input format: Natural number n and two complex numbers z1 and z2, each on a separate line.
# Output format: The program should output the answer to the task.
# Note: \bar{z1} is the conjugate of z1.


# Test ________________________________________________

n = int(input())
z_1 = complex(input())
z_2 = complex(input())

complex_sum = z_1**n + z_2**n + (z_1**n).conjugate() + (z_2 ** (n + 1)).conjugate()
print(complex_sum)
