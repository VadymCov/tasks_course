# 🔢 Interesting Sorting-2
# A string of natural numbers is input to the program. A list of numbers is formed from the elements of the string.
# Write a program to sort the list of numbers in non-decreasing order of the sum of their digits. If two numbers have the same sum of digits, output them in non-decreasing order.
# Input Format:
# A line of text containing natural numbers separated by spaces.
# Output Format:
# The sorted list of numbers, with elements separated by a single space.

# Test ___________________________________

def addition_sort(item):
    return sum([int(i) for i in str(item)]), int(item)
    
n = [int(i) for i in input().split()]

print(sorted(n,key=addition_sort))

