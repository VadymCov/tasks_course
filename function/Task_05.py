# 🔢 Round List Elements with map()
# Write a program that uses the map()
# function to round all elements of the
# list numbers to 2 decimal places, and then prints them, each on a separate line.


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def my_round(num):
    return round(num, 2)


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(my_round, numbers), sep="\n")
