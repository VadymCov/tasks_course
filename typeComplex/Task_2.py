# 🔢 Complex numbers in list
# Complex numbers are stored in the list 'numbers'.
# Complete the given code so that it outputs the complex number with the largest modulus and the modulus itself on separate lines.
# Note: The modulus of a complex number can be calculated using the built-in function abs().


numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# Test ____________________________________________
max_num = numbers[0]
for i in numbers:
    if abs(max_num) < abs(i):
        max_num = i
print(max_num, abs(max_num), sep="\n")

# Test_2 ___________________________________________
max_num = max(numbers, key=abs)
mod_num = abs(max_num)
print(max_num, mod_num, sep="\n")