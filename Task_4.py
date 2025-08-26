# Josephus Problem 🌶️🌶️
# n people, numbered from 1 to n, stand in a circle. 
# They start counting, and every k-th person is eliminated from the circle. 
# The count then continues with the next person. 
# Write a program that determines the number of the person who remains last in the circle.     

n, k = int(input()), int(input())
m = list(range(1, n+1 ))

pos = 0

while len(m) > 1:
    j = (pos + k - 1) % len(m)
    del m[j]
    pos = j % len(m)

print(m) 
