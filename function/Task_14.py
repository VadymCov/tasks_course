# 🌐 Inside the Sphere
# Input to the program: three lines of text with floating-point numbers for x (abscissas), y (ordinates), and z (applicates) of 3D points.
# Write a program to check if all points are inside or on the sphere centered at origin with radius R=2.

# Input Format: Three lines with space-separated floats – x coords, y coords, z coords.

# Output Format: True if all points satisfy x² + y² + z² ≤ 4, else False.

# Note 1: Equal number of values in each line guaranteed.
# Note 2: Sphere equation: x² + y² + z² = R².
# Note 3: Use all() and zip() for solution.

abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())

R = 2
my_list = []
for x, y, z in zip(abscissas, ordinates, applicates):
    if sum((x**2,y**2,z**2)) > R ** 2:
        my_list.append(False)
print(all(my_list))