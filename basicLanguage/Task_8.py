# Shift in development
# The program receives a line of natural numbers as input.
# It creates a list from these elements and performs a cyclic right shift:
# the last element becomes the first, and all others move one position forward
# (towards increasing indices).


n = [int(k) for k in input().split() if k.isdigit()]
last_digit = n.pop()
n.insert(0, last_digit)

print(*n)