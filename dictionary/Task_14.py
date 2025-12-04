# 🔢 **Sequential Number**
# Given a text string in English, consisting of words and space characters. 
# A word is considered to be a sequence of letters, words are separated by 
# one space or several. Write a program that determines for each word the 
# sequential number of its occurrence in the text in exactly this form, 
# **case sensitive**. For the first occurrence of a word, the program will 
# output 1, for the second occurrence of the same word - 2, etc.
# 
# **Input Format**
# The program receives a single line of text consisting only of English 
# letters and space characters.
# 
# **Output Format** 
# For each word in the original text, the program outputs one integer - 
# the occurrence number of this word in the text. Numbers should be output 
# on one line separated by spaces.
# 
# **Note.** The number of integers should match the number of words in the original text.

# Test _____________________________________________________

words = input().split()
my_dict = {}

for i in words:
    my_dict[i] = my_dict.get(i, 0) + 1
    
    print(my_dict[i], end=(" "))