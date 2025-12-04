#_______________________________________________________________
# Task 1 
# The Chinese Zodiac assigns an animal to each year in a 12-year cycle.
# One 12-year cycle is shown below. For example, the year 2012 is the Year of the Dragon.
# Chinese Zodiac 12-year cycle: 2000-Dragon, 2001-Snake, 2002-Horse, 2003-Sheep, 2004-Monkey,
# 2005-Rooster, 2006-Dog, 2007-Pig, 2008-Rat, 2009-Ox, 2010-Tiger, 2011-Rabbit

# Write a program that reads a year and displays the name of the corresponding animal. Your program should work correctly for any year,
# not just the ones listed in the table.

year = int(input())

zodiac_animals = [
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit"
]

index = (year - 2000) % 12 
print(zodiac_animals[index])

