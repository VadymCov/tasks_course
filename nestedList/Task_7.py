# 💫 Sublists of a List
# A sublist is a part of another list. It can contain one element, several, or even none. 
# For example, [1], [2], [3], and [4] are sublists of [1, 2, 3, 4]. [2, 3] is also a sublist. 
# But [2, 4] is not, since 2 and 4 are not adjacent (they’re separated by 3). 
# The empty list is a sublist of any list. The list itself is a sublist of itself — so [1, 2, 3, 4] is a sublist of [1, 2, 3, 4].

# The program receives a text string containing characters separated by spaces. 
# From this string, form a list. Write a program that outputs a list containing all possible sublists of the list, including the empty list.

# Input format:
# A text string of characters separated by spaces is given as input.


# a b v
# [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

def sublist(row):
    result = []

    for i in range(len(row)):
        for j in range(i, len(row)):
            sub = row[i:j + 1 ]
            result.append(sub)

    return result

# Test__________

row = input().split()
print(sublist(row))