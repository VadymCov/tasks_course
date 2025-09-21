# 🌶️ **Rarest Word**
# The program receives a line of text. Write a program that outputs the word 
# that appears least frequently, case insensitive. If there are several such 
# words, output the one that is smaller in lexicographic order.
# 
# **Input Format**
# The program receives a line of text.
# 
# **Output Format** 
# The program should output the word (in lowercase) that appears least frequently.
# 
# **Note 1.** The program should not be case-sensitive, words `apple` and `Apple` 
# should be treated as the same.
# 
# **Note 2.** A word is a sequence of letters. Besides words, the text may contain 
# spaces and punctuation marks `.,!?:;-`, which should be ignored. There are no 
# other characters in the text.

import re

my_string = re.sub(r"[^\w\s]", '', input().lower()).split()

my_dict = {}

for s in sorted(my_string):
    my_dict[s] = my_dict.setdefault(s, 0 ) + 1

min_num = min(my_dict.values())
result = {}

for k, v in my_dict.items():
    if my_dict[k] == min_num:
        result[v] = k
        print(result[v])
        break