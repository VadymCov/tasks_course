# Back, forth, and vice versa
# The program receives a line of non-negative numbers as input.
# It creates a list from these elements and swaps each pair of adjacent elements
# (a[0] with a[1], a[2] with a[3], and so on).
# If the list has an odd number of elements, the last one remains in place.


n = [int(k) for k in input().split() if k.isdigit()]

for i in range(len(n)):
    if i % 2 != 0:
        n[i-1],n[i] = n[i], n[i-1]

print(*n)