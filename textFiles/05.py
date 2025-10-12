# 🔢 Line Numbering You have access to a text file input.txt consisting of several lines.
# Write a program to write the contents of this file to output.txt as a numbered list,
# where each line is preceded by its number, the symbol ) and a space.
# Line numbering should start from 1.
# Input format: The program reads from input.txt.
# Output format: The program creates output.txt with numbered lines.

with open("input.txt", "r", encoding="UTF-8") as f, open("output.txt", "w") as new_f:
    list_text = f.read().split("\n")
    for i, line in enumerate(list_text, start=1):
        new_f.write(f"{i}) {line}\n")
