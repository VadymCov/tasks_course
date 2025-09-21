# 🌶️ **Duplicate Fixing**
# The program receives a string containing identifier strings. Write a program 
# that fixes them so that there are no duplicates in the resulting string. 
# To do this, you need to add the postfix `_n` to repeating identifiers, 
# where `n` is the number of times such identifier has already appeared.
# 
# **Input Format**
# The program receives a line of text containing identifier strings separated 
# by spaces.
# 
# **Output Format** 
# The program should output the corrected string without duplicates while 
# preserving the original order.

ind = input().split()

dict = {}

for i in ind:
    dict[i] = dict.get(i, '')
print(dict)