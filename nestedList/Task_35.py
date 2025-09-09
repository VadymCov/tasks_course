# 📝 **Every n-th Element**
# The program receives a text string containing symbols and a number n as input. 
# A list is formed from this string. Write a program that divides the list into 
# nested sublists so that n consecutive elements belong to different sublists.
# **Input format** The program receives a text string containing symbols separated 
# by a space character, and the number n on a separate line.
# **Output format** The program should output the specified nested list.


row = input().split()
num = int(input())

matrix = [[] for _ in range(num)]
n = len(row)
for i in range(num):
    temp = []
    for j in range(i, n, num):
        matrix[i].append(row[j])
    
print(matrix)
