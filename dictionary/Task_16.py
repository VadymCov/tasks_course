# 🔎 **Query String**
# A query string is part of a URL address containing keys and their values. 
# It starts after the question mark and goes to the end of the address. For example:
# 
# https://example.com?name=alex                 # query string: name=alex
# 
# If there are multiple parameters in the query string, they are separated 
# by an ampersand `&`:
# 
# https://example.com?name=alex&color=blue     # query string: name=alex&color=blue 
# 
# Write a function `build_query_string()` that takes a dictionary with parameters 
# as input and returns a query string formed from these parameters.
# 
# **Note 1.** In the final string, parameters should be sorted in lexicographic 
# order of dictionary keys.
# 
# **Note 2.** The following program code:
# 
# print(build_query_string({'name': 'alex', 'age': 25}))
# print(build_query_string({'sport': 'tennis', 'game': 3, 'time': 15}))
# 
# should output:
# 
# age=25&name=alex
# game=3&sport=tennis&time=15


# Test ____________________________________________________-

def build_query_string(par):
    result = ''
    for k, v in sorted(par.items()):
        result += f"{k}={v}&"

    return result.rstrip('&')
