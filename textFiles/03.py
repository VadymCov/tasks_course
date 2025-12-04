# 📝 Task: CSV File Reader 📂

# Objective: Write a function 'read_csv()' to read data from the file 'data.csv'.
# The function must return a list of dictionaries.
# - The first row of the CSV file serves as the dictionary keys.
# - Each subsequent row serves as the values for those keys.

import csv


def read_csv(file: str = "data.csv") -> list[dict[str, str]]:
    with open(file, "r", encoding="UTF-8") as f:
        list_dictionary: list[dict[str, str]] = []
        reader = csv.reader(f)
        keys = next(reader)
        for lines in reader:
            my_dict = zip(keys, lines)
            list_dictionary.append(dict(my_dict))
        return list_dictionary
