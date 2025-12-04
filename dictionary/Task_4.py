# 📡 **Morse Code**
# Morse code uses dashes and dots to represent digits and letters.
# Write a program to encode a text message according to Morse code.
# 
# Symbol | Code  | Symbol | Code  | Symbol | Code  | Symbol | Code
# A      | .-    | J      | .---  | S      | ...   | 1      | .----
# B      | -...  | K      | -.-   | T      | -     | 2      | ..---
# C      | -.-.  | L      | .-..  | U      | ..-   | 3      | ...--
# D      | -..   | M      | --    | V      | ...-  | 4      | ....-
# E      | .     | N      | -.    | W      | .--   | 5      | .....
# F      | ..-.  | O      | ---   | X      | -..-  | 6      | -....
# G      | --.   | P      | .--.  | Y      | -.--  | 7      | --...
# H      | ....  | Q      | --.-  | Z      | --..  | 8      | ---..
# I      | ..    | R      | .-.   | 0      | ----- | 9      | ----.
# 
# **Input Format**
# The program receives one line - a text message.
# 
# **Output Format** 
# The program should output the message encoded using Morse code, leaving 
# a space between each encoded character (sequence of dashes and dots).
# 
# **Note 1.** Your program should ignore the case of characters in the original text message.
# 
# **Note 2.** Your program should ignore any characters not listed in the table.
# 
# **Note 3.** Morse code was developed in the 19th century and is still used, 
# more than 160 years after its creation.

# Test ______________________________________________________________-

dictionary = {
    'A': '.-',	'J': '.---','S': '...',	 '1': '.----',
    'B': '-...','K': '-.-',	'T': '-',	 '2': '..---',
    'C': '-.-.','L': '.-..','U': '..-',	 '3': '...--',
    'D': '-..',	'M': '--',	'V': '...-', '4': '....-',
    'E': '.',	'N': '-.',	'W': '.--',	 '5': '.....',
    'F': '..-.','O': '---',	'X': '-..-', '6': '-....',
    'G': '--.',	'P': '.--.','Y': '-.--', '7': '--...',
    'H': '....','Q': '--.-','Z': '--..', '8': '---..',
    'I': '..',	'R': '.-.',	'0': '-----','9': '----.'
}

text_sms = input().upper()
for j in text_sms:
    for key, value in dictionary.items():
        if j == key:
            print(value, end=" ")
            break