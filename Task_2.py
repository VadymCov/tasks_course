#_______________________________________________________________    
# Task 2
# Number Reversal 🔄
# Given a five- or six-digit natural number, write a program that reverses the order of its last five digits.n = int(input())
s = str(n)
res = 0
if len(s) == 5:
    res += int(s[::-1])
else:
    res += int(s[0] + s[1:][::-1])
print(res)