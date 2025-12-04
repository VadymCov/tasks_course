# 💻 Sort as you like

# The list athletes contains information about athletes as tuples: (name, age, height, weight).

# Write a program to sort the list of athletes by the specified field:
# 1: by name;
# 2: by age;
# 3: by height;
# 4: by weight.

# Input format
# The program receives a natural number from 1 to 4 – the field number by which to sort the list.

# Output format
# The program should output the list sorted by the specified field according to the examples.

# Note. Solve the task without using a conditional operator.

# Test __________________________________________
athletes = [
    ("Mike", 10, 130, 35),
    ("John", 11, 135, 39),
    ("Alex", 9, 140, 33),
    ("David", 10, 128, 30),
    ("James", 16, 170, 70),
    ("Robert", 16, 188, 100),
    ("Matthew", 17, 168, 68),
    ("Peter", 15, 190, 90),
]


def name(ath):
    return ath[0]


def age(ath):
    return ath[1]


def height(ath):
    return ath[2]


def weight(ath):
    return ath[3]


all_func = (name, age, height, weight)
result = sorted(athletes, key=all_func[int(input())])
for i in result:
    print(*i)
