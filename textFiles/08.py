"""
File Concatenation 📂🔥

The program receives a natural number n and n strings with file names as input. Write a program that creates a file output.txt and outputs the contents of all files to it without changing their order.

Input Format:
The program receives a natural number n and n strings of names of existing files.

Output Format:
The program should create a file named output.txt in accordance with the task condition.
"""

all_name_files = [input() for _ in range(int(input()))]

with open("output.txt", "w", encoding="UTF-8") as new_f:
    for file in all_name_files:
        with open(file, "r", encoding="UTF-8") as f:
            new_f.write(f.read())
