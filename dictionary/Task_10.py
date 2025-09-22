# 🌍 **Countries and Cities**
# The program receives a list of countries and cities of each country as input. 
# Then city names are given. Write a program that for each city outputs which 
# country it is located in.

# **Input format** 
# The program receives the number of countries n as input. Then follow n lines, 
# each line starts with the name of a country, followed by the names of cities 
# in that country. The next line contains the number m, followed by m queries - 
# names of some m cities from those listed above.

# Test_______________________________________________________________

num = int(input())
my_dict = {}

for _ in range(num):
    countries, *cities = input().split()
    for i in cities:
        my_dict[i] = countries

num_cities = int(input())

result = []

for _ in range(num_cities):
    result.append(my_dict.get(input(), 'there is no such country'))
print(*result, sep="\n")

    