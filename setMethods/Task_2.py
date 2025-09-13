# 🔤 Unique Characters Counter 🎯
# 
# A text analyzer needs to count how many different letters appear in each word,
# ignoring whether they're uppercase or lowercase.
# This program helps identify the diversity of characters in various words.
#
# Input:
#   The first line contains an integer n - the total number of words.
#   Then follow n lines with words.
#
# Output:
#   The program should output on a separate line the number of unique characters for each word.



#Test_1____________________________
n = int(input())

for i in range(n):
    word = input().lower()
    print(len(set(word)))


#Test_2___________________________

words = [set(input().lower()) for _ in range(int(input()))]

for k in words:
    print(len(set(k)))
