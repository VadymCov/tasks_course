# # 🔢 **Number of Matches**
# # The program receives two lines of text containing numbers. Write a program that determines 
# # the number of numbers that are present in both the first line and the second line.
# # 
# # **Input Format**
# # The program receives two lines of text containing numbers separated by spaces.
# # 
# # **Output Format** 
# # The program should output the number of numbers contained simultaneously 
# # in both the first line and the second line.
# # Test _____________________________________________________

s1, s2 = set(input().split()), set(input().split())
s1.intersection_update(s2)
print(len(s1))
# #___________________________________________________________



# # 🔢 **Common Numbers**
# # The program receives two lines of text containing numbers. Write a program that outputs 
# # all numbers in ascending order that are present in both the first line and the second line.
# # 
# # **Input Format**
# # The program receives two lines of text containing integers separated by spaces.
# # 
# # **Output Format** 
# # The program should output on one line, separated by spaces, the numbers that appear 
# # in both lines.

# # Test____________________________________________________

s1, s2 = [set(map(int, input().split())) for _ in ['s1', 's2']]
result = sorted(s1.intersection(s2))
print(*result)
# #_________________________________________________________



# 🔢 **Numbers of the First Line**
# The program receives two lines of text containing numbers. Write a program that outputs 
# all numbers in ascending order that are present in the first line but absent in the second.
# 
# **Input Format**
# The program receives two lines of text containing numbers separated by spaces.
# 
# **Output Format** 
# The program should output the set of numbers that appear only in the first line.


# # Test____________________________________________________

s1, s2 = [set(map(int, input().split())) for _ in range(2)]
print(*sorted(s1.difference(s2)))
#_____________________________________________________________



# 🔢 **Common Digits**
# The program receives a natural number n, and then n different natural numbers, 
# each on a separate line. Write a program that outputs all common digits in 
# ascending order among all entered numbers.

# **Input Format**
# The program receives a natural number n (n≥1), and then n different natural numbers, 
# each on a separate line.

# **Output Format** 
# The program should output the digits according to the task condition. 
# If there are no common digits, then nothing should be output.


# # Test________________________________________________________

n = int(input())

my_list = [str(int(input())) for _ in range(n)]
my_set = set(my_list[0])

for i in range(1,n):
    my_set &= set(my_list[i])
    
print(*sorted(my_set))
#_______________________________________________________________