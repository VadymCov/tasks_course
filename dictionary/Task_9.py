# 📖 **Synonym Dictionary**
# You are given a dictionary consisting of pairs of synonym words. There are no 
# duplicate words in the dictionary. Write a program that determines the synonym 
# of one given word.

# **Input format** 
# The program receives the number of synonym pairs n as input. This is followed 
# by n lines, each line containing two synonym words. After that follows one word 
# whose synonym needs to be found.

# **Output format** 
# The program should output one word, the synonym of the entered word.

# **Note 1.** It is guaranteed that the synonym of the entered word exists in 
# the dictionary.
# **Note 2.** All words in the dictionary start with a capital letter.

# Test__________________________________________

num = int(input())
dict_syn = {}

for i in range(num):
    k, v = input().title().split()
    dict_syn[k] = v 
    dict_syn[v] = k

print(dict_syn[input()])
