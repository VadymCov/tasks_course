#_______________________________________________________________    
# Task 3
# Standard American Convention
# A natural number is given as input. Write a program that inserts commas into the number 
# according to the standard American convention for large numbers.

n = input()[::-1]

count = 0 
result = ''

for i in n:
    if count == 3:
        result += ','
        count = 0
        
    count += 1
    result += i

print(result[::-1]) 
