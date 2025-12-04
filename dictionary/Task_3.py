# 📩 **Text Message Typing**
# On mobile keypad phones, text messages can be sent using the numeric keypad. 
# Since multiple letters are associated with each key, most letters require 
# multiple key presses. Pressing a digit once generates the first character 
# listed for that key. Pressing a digit 2, 3, 4, or 5 times generates the 
# second, third, fourth, or fifth character of the key.
# 
# 1: `.,?!:`
# 2: `ABC`
# 3: `DEF`
# 4: `GHI`
# 5: `JKL`
# 6: `MNO`
# 7: `PQRS`
# 8: `TUV`
# 9: `WXYZ`
# 0: `space`
# 
# Write a program that displays the key presses required for the entered message.
# 
# **Input Format**
# The program receives one line - a text message.
# 
# **Output Format** 
# The program should output the key presses required for the entered message.
# 
# **Note 1.** Your program should handle both uppercase and lowercase letters.
# 
# **Note 2.** Your program should ignore any characters not listed in the table above.

# Test_______________________________________________________________________

dictionary = {
    '1':	'.,?!:',
    '2':	'ABC',
    '3':	'DEF',
    '4':	'GHI',
    '5':	'JKL',
    '6':	'MNO',
    '7':	'PQRS',
    '8':	'TUV',
    '9':	'WXYZ',
    '0':	' ' 

}

sms = input().upper()

for i in sms:
    for key, value in dictionary.items():
        if i in value:
            print(key * (value.find(i) + 1), end="")
            break