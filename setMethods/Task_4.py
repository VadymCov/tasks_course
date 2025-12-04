# 📚 Word Diversity Analyzer 🔍
# 
# A text processing system needs to count how many different words appear in a given text,
# ignoring case differences and punctuation marks.
# This program helps analyze vocabulary richness in any text input.
#
# Input:
#   A single line of text.
#
# Output:
#   The program should output one number - the total count of different words 
#   in the text, case-insensitive.
#
# Note 1: A word is considered to be a sequence of non-space characters going in a row,
#         words are separated by one or more spaces.
# Note 2: Punctuation marks .,;:-?! are ignored.

s = input().lower()

signs = ".,;:-?!"
processed_text = ''

for k in s:
    if k not in signs:
        processed_text += k

print(len(set(processed_text.split())))