# 🌶️ **Dictionary Merge**
# Write a function `merge()` that combines dictionaries into one general dictionary. 
# The function should take a list of dictionaries and return a dictionary where 
# each key contains a set (data type `set`) of unique values collected from 
# all dictionaries in the passed list.
# 
# **Note 1.** The following program code:
# 
# result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# 
# creates a dictionary:
# 
# result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
# 
# **Note 2.** You don't need to call the `merge()` function, just implement it.
# 
# **Note 3.** Merging empty dictionaries should result in an empty dictionary.

# Test ______________________________________-

def merge(value):

    my_dict = {}
    
    for d in value:
        for k, v in d.items():
            my_dict[k] = my_dict.setdefault(k, set([v])).union([v])
    return my_dict

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))