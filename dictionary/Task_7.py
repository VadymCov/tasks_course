# 📘 **Programmer's Dictionary**
# Programmers, as you already know, are constantly learning, and in communication 
# with each other they use quite specific language. To systematize your growing 
# professional lexicon, we came up with this task. Write a program to create a 
# small dictionary of slang programming expressions, so that it can later return 
# values from this dictionary upon request.

# **Input format** 
# The first line contains one integer n - the number of words in the dictionary. 
# The next n lines contain words and their definitions, separated by a colon and 
# a space. The next line contains an integer m - the number of search words whose 
# definition needs to be output. The next m lines contain the words themselves, 
# one per line.

# **Output format** 
# For each word, regardless of case, if it is present in the dictionary, you need 
# to output its definition. If the word is not in the dictionary, the program 
# should output "Not found" (without quotes).

# Test  _______________________________________________________________


n = int(input())
prg_dict = {}

for i in range(n):
    user_input = input().split(':')
    prg_dict[user_input[0].capitalize()] = user_input[1].strip()

request = [input().capitalize() for _ in range(int(input()))]
for i in request:
    print(prg_dict.get(i, "Not found"))

