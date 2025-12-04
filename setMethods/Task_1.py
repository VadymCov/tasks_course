# 👨‍🎓✍ The 10th grade students of school #10 attended sports sections in the summer: football, basketball and volleyball.
# n students played football,
# m students played basketball,
# k students played volleyball.
#
# It is also known that:
# x students played football or basketball, or both,
# y students played basketball or volleyball, or both,
# z students played football or volleyball, or both,
# t students attended all three sports sections.
#
# There are a students in the class.
# Write a program that determines:
# 1. How many students played only one sport.
# 2. How many students played exactly two sports.
# 3. How many students did not play any of these three sports.

#👇logic on decisions


n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

ab = n + m - x - t
bc = m + k - y - t 
ca = k + n - z - t

one_sport =  n + m + k  - ((ab + ca + bc) * 2 + t * 3)
two_sport = ab + bc + ca
not_sport = a - (one_sport + two_sport + t)

print(one_sport, two_sport, not_sport, sep="\n")