# 🔐 **Secret Word**
# Write a program to decrypt a secret word using frequency analysis method.
# 
# **Input Format**
# The first line contains an encrypted word. The second line contains one integer n - 
# the number of letters in the dictionary. The next n lines contain how many times 
# a specific letter of the alphabet appears in this word - `<letter>: <frequency>`.
# 
# **Output Format** 
# The program should output the decrypted word.
# 
# **Note.** It is guaranteed that letter frequencies do not repeat.

word = input()
my_dict = {}

for _ in range(int(input())):
    key, value = input().split(':')
    my_dict[int(value)] = key

for i in word:
    key = word.count(i)
    print(my_dict[key], end=(""))