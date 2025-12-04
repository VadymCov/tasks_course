# 🐍 Select all three-digit numbers from the list numbers that leave a remainder of 2 when divided by 5, using the filter() function.
# Then, use the map() function to compute the cube of each selected number.
# Finally, print each cube on a separate line.
# Note: The condition about the remainder must apply to the original number, not its cube.
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def process_numbers(num):
    if (
        len(str(num)) == 3 and
        num % 5 == 2
    ):
        return num

def cubing(item):
    return item ** 3

numbers = [
    1014, 1321, 675, 1215, 56, 1386,
    1385, 431, 1058, 486, 1434, 696,
    1016, 1084, 424, 1189, 475, 95,
    1434, 1462, 815, 776, 657, 1225,
    912, 537, 1478, 1176, 544, 488,
    668, 944, 207, 266, 1309, 1027,
    257, 1374, 1289, 1155, 230, 866,
    708, 144, 1434, 1163, 345, 394,
    560, 338, 232, 182, 1438, 1127,
    928, 1309, 98, 530, 1013, 898,
    669, 105, 130, 1363, 947, 72,
    1278, 166, 904, 349, 831, 1207,
    1496, 370, 725, 926, 175, 959,
    1282, 336, 1268, 351, 1439, 186,
    273, 1008, 231, 138, 142, 433,
    456, 1268, 1018, 1274, 387, 120,
    340, 963, 832, 1127
    ]
print(*map( cubing, (filter(process_numbers, numbers))), sep="\n")