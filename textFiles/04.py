# 🎲 Random Numbers
# Write a program that saves 25 random integers in the range from 111 to 777 (inclusive)
# to a text file named random.txt, each number on a new line.
#
# Input format: No input is provided to the program.
# Output format: The program should create a file named random.txt and write random numbers to it.

import random

with open("random.txt", "r+") as f:
    numbers = random.choices(range(111, 778), k=25)
    for line in numbers:
        f.writelines(str(line) + "\n")
