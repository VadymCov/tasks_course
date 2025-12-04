# 🎁 New Year's gift
#
# You have a text file class_scores.txt with test results in the format:
# surname score (separated by a space). Score is an integer from 0 to 100 inclusive.
#
# Write a program to add 5 points to each test result and output surnames and new scores to the file new_scores.txt.

with open("class_scores.txt", "r", encoding="UTF-8") as file, open("new_scores.txt", "w", encoding="UTF-8") as new_file:
    list_file = file.read().split()
    for i, elem in enumerate(list_file):

        if elem.isdigit():
            elem = int(elem) + 5

            if elem > 100:
                elem = 100
            elem = " " + str(elem)

            if i < len(list_file) - 1:
                elem += "\n"
        new_file.write(elem)
