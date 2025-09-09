# 🪙 Heads or Tails
# The program receives a string consisting only of the Russian letters "О" and "Р".
# "О" stands for heads, "Р" stands for tails.
# Your task is to determine the longest sequence of consecutive tails ("Р") in the string.

s = input()
n = s.split("О")
print(len(max(n)))