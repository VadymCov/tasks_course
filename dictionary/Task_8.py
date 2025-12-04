# 🔄 **Anagrams 1**
# An anagram is a word (phrase) formed by rearranging the letters that make up 
# another word (or phrase). For example, the English words `evil` and `live` 
# are anagrams.
# The program receives two words as input. Write a program that determines 
# whether they are anagrams.

# **Input format** 
# The program receives two words as input, each on a separate line.

# **Output format** 
# The program should output `YES` if the words are anagrams, or `NO` otherwise.


# Test __________________________________________

first_word = input()
second_word = input()

first_word_dict = {}
for i in first_word:
    first_word_dict[i] = first_word_dict.get(i, 0) + 1

second_word_dict = {}
for j in second_word:
    second_word_dict[j] = second_word_dict.get(j, 0) + 1

print(("NO", "YES")[first_word_dict == second_word_dict])
