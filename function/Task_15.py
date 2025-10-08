# 📡 Valid IP Address
# An IP address is a unique numeric identifier for a device in a computer network using the TCP/IP protocol.

# In version 4, the IP address is a 32-bit number.
# It is written as four decimal numbers (octets) ranging from 0 to 255 (inclusive), separated by dots, e.g., 192.168.1.2.

# Write a program using the built-in all() function to check the validity of an IP address: whether all octets are numbers from 0 to 255.

# Input Format: A string in the format x.x.x.x, where x is a non-empty set of characters 0-9, a-z.

# Output Format: True if the input string is a valid IP address, False otherwise.

# Note: Leading zeros should be ignored.

num = input().split(".")
my_list =[]
if len(num) == 4:
    for i in num:
        my_list.append(i.isdigit() and 0 <= int(i) <= 255 )
    print(all(my_list))
else:
    print(False)