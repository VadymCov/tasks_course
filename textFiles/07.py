"""
Riddle from Jacqui Fresco 🐐🌶️

Once Jacqui Fresco was asked:
"If you're so smart, why aren't you rich?"
Jacqui chose not to answer this provocative question and instead posed a riddle:
"There were multicolored goats. How many?"
"How many what?"
"How many of them make up more than 7% of the total number of goats?"

You are given a text file 'goats.txt' where:
- The first line contains the word 'COLOURS'
- Followed by a list of all possible goat colors
- Then comes a line with the word 'GOATS'
- Followed by the enumeration of goats of different colors

The list of goats only includes colors from the first list.

Write a program to create a file 'answer.txt' and output the list of goat colors that satisfy Jacqui Fresco's riddle condition.

Input Format:
The program takes no input.

Output Format:
The program should create a file named 'answer.txt' and write the names of goat colors that satisfy the condition in alphabetical order.
"""

with open("goats.txt", "r", encoding="UTF-8") as f, open("answer.txt", "w", encoding="UTF-8") as n_f:
    file = f.readlines()
    all_colours, all_goats = file[1:file.index("GOATS\n")], file[file.index("GOATS\n") + 1:]
    list_answer: list[str] = []
    for i in all_colours:
        if (all_goats.count(i) * 100) > (len(all_goats) * 7):
            list_answer.append(i)


    n_f.writelines(sorted(list_answer))