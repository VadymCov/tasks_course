# Distinct elements
# The program receives a line of natural numbers in non-decreasing order.
# It creates a list from these numbers and counts how many distinct elements it contains.
#
# Input format:
# A line of natural numbers separated by spaces, arranged in non-decreasing order.

n = input().split()
result = []

for i in n:
    if i not in result:
        result.append(i)
        
print(len(result))