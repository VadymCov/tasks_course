# 🗺️ Unusual Countries
# Here's the Python program to solve the task, followed by the English translation of the
# task and the code explanation.

with open("population.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        list_line = line.split()
        if int(list_line[-1]) > 500_000 and list_line[0].startswith("G"):
            print(*list_line[0:1])