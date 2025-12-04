# Coordinate Quadrants
# Given a set of points on a coordinate plane, count and output the number of points
# located in each of the four coordinate quadrants.
#
# Input format:
# The first line contains the number of points.
# Each of the following lines contains two integers — the coordinates of a point
# (first the x-coordinate, then the y-coordinate), separated by a space.
  
number_of_points = int(input())
quarter_1 = 0
quarter_2 = 0
quarter_3 = 0
quarter_4 = 0

for i in range(number_of_points):
    coordinates = input().split()
    x = int(coordinates[0])
    y = int(coordinates[1])

    if x > 0 and y > 0:
        quarter_1 += 1

    elif x < 0 and y > 0:
        quarter_2 += 1

    elif x < 0 and y < 0:
        quarter_3 += 1

    elif x > 0 and y < 0:
        quarter_4 += 1

print(f"First quarter: {quarter_1}\nSecond quarter: {quarter_2}\nThird quarter: {quarter_3}\nFourth quarter: {quarter_4}")
