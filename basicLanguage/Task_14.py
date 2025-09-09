# 🤖 Silicon Valley Chronicles:
# Dexter — a rogue AI created by Gilfoyle — has hijacked a network of smart coffee machines.
# He now uses them as nodes for his underground system called "The Pied Piper Protocol".
# Each machine transmits a string of data (lowercase letters and digits).
# If the string contains the word "dexter" as a subsequence (letters appear in order, not necessarily consecutively),
# the machine is considered infected.
# Your mission: identify and print the indices (starting from 1) of all infected machines.

n = int(input())
match_text = "dexter"
result = []

for i in range(n):
    text_input = input()
    temp = 0
    for s in text_input:
        if s == match_text[temp]:
            temp += 1
        if temp == 5:
            result.append(i + 1)
            break

print(*result)
