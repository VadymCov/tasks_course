# 💬 **String Representation**
# Write a program that converts a natural number into a string, replacing 
# all digits in the number with words:
# * 0 to zero;
# * 1 to one;
# * 2 to two;
# * 3 to three;
# * 4 to four;
# * 5 to five;
# * 6 to six;
# * 7 to seven;
# * 8 to eight;
# * 9 to nine.
# 
# **Input Format**
# The program receives a natural number.
# 
# **Output Format** 
# The program should output the string representation of the number.
# 
# **Note.** Use a dictionary instead of conditional operators.

# Test _______________________________________________________

my_dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

num = int(input())

for i in str(num):
    print(my_dict[i], end=" ")
