# 🕵️‍♂️ Secret Friend Program
# Write a program that randomly assigns each student their secret friend 
# who will solve programming problems together with them.

# 📥 Input Format 
# The program receives number n in the first line - total number of students.
# Then n lines follow, containing first and last names of students.

# 📤 Output Format
# The program should output student's first and last name (in original order) 
# and first and last name of their secret friend, separated by hyphen.

# 📝 Note 1: 
# Note that you cannot be a secret friend to yourself 
# and cannot be a secret friend to multiple students.

# 📝 Note 2: 
# The tests below are just samples of possible answers. 
# Other ways of choosing secret friends are also possible.

# Test __________________________________________________

from random import shuffle

n = int(input())

list_name = [input() for _ in range(n)]

mixed_sheet = list(list_name)


while True:
    cnt = n
    for i in range(n):
        if list_name[i] != mixed_sheet[i]:
            cnt -= 1
        else:
            shuffle(mixed_sheet)
            break
    if cnt == 0:
        break

for k in range(n):
    print(f"{list_name[k]} - {mixed_sheet[k]}")