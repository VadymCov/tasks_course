#  💥 Duplicate Packing
#  The program receives a text string as input, containing characters.
#  Write a program that packs consecutive identical characters of the given string into sublists.
#
#  Input format:
#  A text string is input, with characters separated by a space.

# a a a d d d
# [["a", "a", "a"], ["d", "d", "d"]]

def duplicate_packing(n):

    result = []
    temp_result = []

    for i in n:
        if (len(temp_result) == 0) or (i in temp_result):
            temp_result.append(i)
        else:
            result.append(temp_result[:])
            temp_result.clear()
            temp_result.append(i)
    result.append(temp_result)
    return result

#_______________________________    
n = input().split()
print(duplicate_packing(n))