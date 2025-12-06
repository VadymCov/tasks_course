# 🔢 Interesting Sorting-1
# A string of natural numbers is input to the program. A list of numbers is formed from the elements of the string.
# Write a program to sort the list of numbers in non-decreasing order of the sum of their digits. If two numbers have the same sum of digits, preserve their relative positions in the original list.
# Input Format:
# A line of text containing natural numbers separated by spaces.
# Output Format:
# The sorted list of numbers, with elements separated by a single space.


# Test________________________________________________________________

n = input().split()

def addition_sort(item):
    res = 0
    for i in item:
        res += int(i)
    return(res)

print(*sorted(n, key=addition_sort))
