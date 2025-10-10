"""
🤖 GEMATRIA WORD SORT 🤖

Task: Sort a list of English words based on their Gematria value.

Gematria is the sum of the numerical values of the letters in a word.

## Gematria Calculation Rules:
1.  Convert the word to **UPPERCASE**.
2.  The numerical value of a letter is calculated as:
    (Code of the letter) - (Code of the letter 'A').
    (e.g., Value('A') = ord('A') - ord('A') = 0.
    Value('B') = ord('B') - ord('A') = 1, etc.)
3.  The word's Gematria is the SUM of these individual letter values.

## Sorting Rules (The 'Key' for sorting):
1.  **Primary Key:** Sort by Gematria value in **ASCENDING** order.
2.  **Secondary Key (Tie-breaker):** If Gematria values are equal, sort by the original word in **ALPHABETICAL (lexicographical)** order.

The output must display the words in their original case, each on a new line.

## Implementation Notes:
-   The program first reads an integer N (the number of words).
-   It then reads N lines (the words).
-   Use the built-in function ord() to get the character code.
-   Words may be repeated in the input.

Example: For "BaSis" -> "BASIS"
Gematria = (ord('B')-ord('A')) + (ord('A')-ord('A')) + (ord('S')-ord('A')) + (ord('I')-ord('A')) + (ord('S')-ord('A'))
"""


def my_sort(iterable):
    primary_key = 0
    for i in iterable:
        primary_key += ord(i.upper()) - ord("A")
    secondary_key = iterable
    return primary_key, secondary_key


words = [input() for _ in range(int(input()))]

my_sorted = sorted(words, key=my_sort)
print(*my_sorted, sep="\n")
