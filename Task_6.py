# Greater than the previous
# The program receives a line of natural numbers as input.
# It forms a list of numbers and counts how many of them are greater than
# the number immediately preceding them in the list.

n = [int(k) for k in input().split() if k.isdigit()]

res = 0
li = [0]

for i in n:
    if i > li[0]:
        res += 1
        li[0] = i
    else:
        li[0] = i
        
print (res - 1)