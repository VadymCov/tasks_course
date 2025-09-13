# 🌐 Global Character Collector 📊
# 
# A linguistic researcher wants to find out how many different letters appear
# across an entire collection of words, treating uppercase and lowercase as the same.
# This program analyzes the alphabet diversity in a word dataset.
#
# Input:
#   The first line contains an integer n - the total number of words.
#   Then follow n lines with words.
#
# Output:
#   The program should output one number - the total count of unique characters 
#   across all words, case-insensitive.



# Test__________________________

n = int(input())

words = ''

for k in range(n):
    words += input().upper()
print(len(set(words)))

    
    