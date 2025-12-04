# 🔰 The list 'data' contains information about the population of some US states.
# Write a program to sort the 'data' list in descending order based on the last
# character of the state name. Then, print the elements of this list, each on a
# new line, in the format: <state name>: <population>.
# Note 1: The sorting is performed in descending lexicographical order based on
# the last character of the state name. If two states have the same last character,
# their relative order in the initial list should be preserved (stable sort).
# Note 2: Use an anonymous function (lambda) as the sort key.

data = [
    (19542209, "New York"),
    (4887871, "Alabama"),
    (1420491, "Hawaii"),
    (626299, "Vermont"),
    (1805832, "West Virginia"),
    (39865590, "California"),
    (11799448, "Ohio"),
    (10711908, "Georgia"),
    (10077331, "Michigan"),
    (10439388, "Virginia"),
    (7705281, "Washington"),
    (7151502, "Arizona"),
    (7029917, "Massachusetts"),
    (6910840, "Tennessee"),
]

func_sort = sorted(data, reverse=True,key=lambda x: x[1][-1])
for item in func_sort:
    index, cities = item
    print(f"{cities}: {index}")
