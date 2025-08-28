# 🎶 The Letter Ban Song 🚫
# 
# A quirky censorship bot has started banning letters from the alphabet one by one.
# This program simulates a song where each line ends with the next banned letter (in alphabetical order),
# and that letter is removed from the phrase in the next iteration.
#
# Input:
#   A single word consisting of lowercase English letters.
#
# Output:
#   For each unique letter (in alphabetical order) found in the initial phrase:
#     - Print the current phrase with the banned letter added at the end.
#     - Remove that letter from the phrase before the next iteration.

alphabet = "abcdefghijklmnopqrstuvwxyz"

word = input()

text_song = word + " has banned the letter"

for ch in alphabet:
    if ch in text_song:
        print(" ".join((text_song + " " + ch).split()))
        text_song = text_song.replace(ch, "")
