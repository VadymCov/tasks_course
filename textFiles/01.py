# 📝 Task: Random Name and Surname Generator 🎲
#
# Available files: 'first_names.txt' and 'last_names.txt' (one with first names, one with last names).
#
# Objective: Write a program using the 'random' module to generate and print 3 random
# full names (first name + last name) in the format "Name Surname", each on a separate line.
#
# Input format: None (no input data provided).
# Output format: 3 lines of text, e.g., "Ivan Petrov".

import random

with open("first_names.txt", "r", encoding="UTF-8") as f_first, open("last_names.txt", "r", encoding="UTF-8") as f_last:

    list_first_name = [n.strip("\n") for n in f_first.readlines()]
    list_last_name = [n.strip("\n") for n in f_last.readlines()]

    first_name = random.choices(list_first_name, k=3)
    last_name = random.choices(list_last_name, k=3)

    for i in range(3):
        print(f"{first_name[i]} {last_name[i]}")
