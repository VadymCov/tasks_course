# 📒 **Phone Book**
# Alex recorded the phone numbers of all his friends to automate the search 
# for the right number. Each of Alex's friends may have one or more phone numbers. 
# Write a program that will help Alex find all the numbers of a specific friend.
# 
# **Input Format**
# The first line contains one integer n - the number of phone numbers whose 
# information Alex saved in the phone book. The next n lines contain phones 
# and names of their owners separated by a space. The next line contains 
# integer m - the number of search queries from Alex. The next m lines contain 
# the queries themselves, one per line. Each query is the name of a friend 
# whose phones Alex wants to find.
# 
# **Output Format** 
# For each query from Alex, output on a separate line all phones belonging 
# to a person with this name (regardless of name case). If there are no phones 
# of a person with this name in the phone book, output "subscriber not found" 
# (without quotes) on the corresponding line.
# 
# **Note 1.** Output phones of one person on one line separated by spaces 
# in the order they were given in the input data.
# 
# **Note 2.** The number of lines in the answer should be equal to m.
# 
# **Note 3.** A phone is several digits written in a row, and a name can 
# consist of letters from the Russian or English alphabet. Records do not repeat.


num = int(input())

my_dict = {}
for _ in range(num):
    number, name = input().split()
    my_dict[name] = my_dict.setdefault(name, []) + [number]

search = [input().capitalize() for _ in range(int(input()))]

for i in search:
    if i in my_dict:
        print(*my_dict[i])
    else:
        print("Subscriber not found")