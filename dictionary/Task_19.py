# 🛒🌶️ **Online Store Shopping**
# Write a program to count the number of units of each type of product purchased 
# by each customer of an online store.
# 
# **Input Format**
# The program receives the number n - the number of rows in the online store sales 
# database. Then follow n lines with records of the form `customer product quantity`, 
# where `customer` is the customer's name (string without spaces), `product` is 
# the product name (string without spaces), `quantity` is the number of product 
# units purchased (natural number).
# 
# **Output Format** 
# The program should output a list of all customers in lexicographic order, 
# after each customer's name - a colon, then a list of names of all products 
# purchased by them in lexicographic order, after each product name - the number 
# of product units. Information about each product is displayed on a separate line.
# 
# **Note.** Pay attention to the second test. If product positions are repeated, 
# then the total quantity of the product for this position gets into the final list.

# Test_______________________________________________

n = int(input())

dict_buyer = {}

for _ in range(n):
    buyer, item, quantity  = input().split()
    
    if buyer not in dict_buyer:
        dict_buyer[buyer] = {}

    if item not in dict_buyer[buyer]:
        dict_buyer[buyer][item] = int(quantity)
    else: 
        dict_buyer[buyer][item] += int(quantity) 

for k in sorted(dict_buyer.keys()):
    print(f"{k}:")
    
    for i in sorted(dict_buyer[k].keys()):
        print(f"{i} {dict_buyer[k][i]}")