# 🏥 **Medical Scanner**
# A medical scanner in a hospital records patient temperature readings every hour. 
# Each time it transmits a positive integer number representing the temperature 
# measurement in tenths of degrees. For proper analysis of results, there is no need 
# to keep duplicate data, so it needs to be removed. Write a program that outputs 
# the maximum number of scanner readings that should be removed so that the result 
# can be properly analyzed.
# 
# **Input Format**
# The program receives one line containing numbers - readings from the medical scanner. 
# Numbers are separated by spaces and do not contain leading zeros.
# 
# **Output Format** 
# The program should output the maximum number of readings that need to be removed 
# so that the analysis of results will be performed correctly.
# 
# **Note.** Consider test example: we have data `365 370 368 365 372 365`. 
# We see that the number 365 appears 3 times - so duplicate numbers 365 need to be removed. 
# We have 2 such duplicates (we don't count the first occurrence of 365). 
# Other numbers don't repeat, so the answer will be 2.

# Test _______________________________________

s = list(map(int, input().split()))

cnt_list = len(s)
cnt_set = len(set(s))
        
print(cnt_list - cnt_set)
# ____________________________________________



# 🎬 **Movie Night**
# Alex and Sam are choosing movies for their weekly movie night. They love 
# watching films and know many titles, especially Alex, but by the end of their 
# discussion they forget which movies they've already mentioned due to excitement.
# Write a program that reads information about their conversation and tells 
# the guys when a movie title is mentioned repeatedly.
# 
# **Input Format**
# The program receives a natural number n in the first line - the number of 
# mentioned movies, then n lines with movie titles, and one more line with 
# a new movie title that was just mentioned.
# 
# **Output Format** 
# The program should output `OK` if this movie hasn't been mentioned yet, 
# or `REPEAT` if the movie has already been named.

# Test ______________________________________

n = int(input())
cities = {input() for _ in range(n)}
next_city = {input()}

if not next_city.isdisjoint(cities):
    print("REPEAD")
else:
    print("OK")

#____________________________________________


# 📚 **Books to Read**
# At the end of the school year, Emma received a summer reading list. Now she needs to
# find out which books on the list she already owns. All the books from Emma's home library are stored in a text file on her computer in random order.
# Write a program that, for each book on the list, determines whether Emma already owns it.
#
# **Input Format**
# The first line of the program receives a positive integer m, the number of books
# in Emma's home library. The second line contains a positive integer n, the number of books on the summer reading list. Then follow m lines with the titles of books from the home library and n lines with the titles of books on the summer reading list.
#
# **Output Format**
# The program should output n lines, each containing the word 'YES' if the book
# was found in the library, or 'NO' if not.


# Test ______________________________________

m, n = [int(input()) for _ in range(2)]
home_library = {input() for _ in range(m)}
summer_list = {input() for _ in range(n)}
for i in summer_list:
    if i in home_library:
        print("YES")
    else:
        print("NO")
#____________________________________________



# 📄 **Strange Hobby**
# As everyone knows, mathematicians are strange people 🤪. No exception is Maya, 
# author of this course. Every day Maya solves exactly two complex mathematical 
# problems. While solving the first problem, she writes down on the first sheet 
# all the numbers that appear in it. Then she takes a break and tackles the second 
# problem. Then she writes down on the second sheet all the numbers that appear 
# in it. After that, she takes another sheet and writes down all the matching 
# numbers from the first two sheets. If such numbers exist - the day was successful, 
# if there are no common numbers - Maya considers the day unsuccessful.
# Write a program that finds common numbers from two sheets or reports that 
# the day was not successful. 😏
# 
# **Input Format**
# The program receives two lines with numbers: the first line contains numbers 
# from the first sheet, the second line contains numbers from the second sheet.
# 
# **Output Format** 
# The program should output numbers that appeared on both sheets in descending 
# sorted order, or the text `BAD DAY` if there are no such numbers.


# Test_______________________________________
s1 = [int(i) for i in input().split()] 
s2 = [int(k) for k in input().split()]

inter_section = set(s1).intersection(set(s2))

if inter_section:
    print(*sorted(inter_section, reverse=True))
else:
    print("BAD DAY")
#____________________________________________



# 👨‍🎓 **Online School SKILLBEE 1**
# When hiring new employees for the online school SKILLBEE, the director tests 
# not only the professional qualities of the candidate, but also their memory.
# The candidate is briefly shown several different numbers, and then the candidate 
# must recall them. It doesn't matter in what order they remember them, and whether 
# they repeat themselves or not, the main thing is that they must name all the numbers 
# without adding extra ones.
# Write a program that determines whether the candidate successfully passed 
# the memory test.
# 
# **Input Format**
# The program receives two lines with numbers: the first line contains numbers 
# shown to the candidate, and the second line contains the candidate's answers.
# 
# **Output Format** 
# The program should output `YES` if the candidate passed the test and can be hired, 
# or `NO` otherwise.

# Test________________________________________

s1 = {int(i) for i in input().split()}
s2 = {int(j) for j in input().split()}

if s1 ^ s2:
    print("NO")
else:
    print("YES")

#_____________________________________________


#  👨‍🎓 **Online School SKILLBEE 2**
# Every student studying at the online school SKILLBEE studies either physics, 
# or chemistry, or both subjects. The school director has lists of students 
# studying each subject.
# Write a program that allows the director to find out how many students 
# study **only physics**.
# 
# **Input Format**
# The program receives numbers m and n in the first two lines - the number of 
# students studying physics and chemistry respectively. Then follow m lines with 
# surnames of students who study physics and n lines with surnames of students 
# studying chemistry.
# 
# **Output Format** 
# The program should output the number of students who study only physics.
# 
# **Note.** It is guaranteed that there are no students with the same surname 
# at SKILLBEE school.

# Test _______________________________________

m, n = [int(input()) for _ in range(2)]

mat = {input() for _ in range(m)}
inf = {input() for _ in range(n)}

print(len(mat.difference(inf)))

#_____________________________________________


# 👨‍🎓 **Online School SKILLBEE 3**
# Every student studying at the online school SKILLBEE studies either biology, 
# or geography, or both subjects. The school director has lists of students 
# studying each subject.
# Write a program that allows the director to find out how many students 
# study **only one subject**.
# 
# **Input Format**
# The program receives numbers m and n in the first two lines - the number of 
# students studying biology and geography respectively. Then follow m lines with 
# surnames of students who study biology and n lines with surnames of students 
# studying geography.
# 
# **Output Format** 
# The program should output the number of students who study only one subject. 
# If there are no such students, then output `NO`.
# 
# **Note.** It is guaranteed that there are no students with the same surname 
# at SKILLBEE school.

# Test________________________________________

m, n = int(input()), int(input())

mat = set([input() for _ in range(m)])
inf = set([input() for _ in range(n)])

result = mat ^ inf

if result:
    print(len(result))
else:
    print("NO")

#_____________________________________________


# 👨‍🎓 **Online School SKILLBEE 4**
# The director of online school SKILLBEE and his assistant are remembering 
# students from their school. For this purpose, each of them made a list of 
# students they remembered.
# Write a program that outputs the surnames of all students that the director 
# and his assistant remembered.
# 
# **Input Format**
# The program receives surnames written by the school director in the first line, 
# and surnames written by his assistant in the second line. Surnames are separated 
# by spaces.
# 
# **Output Format** 
# The program should output surnames of all students from online school SKILLBEE 
# in lexicographic order.
# 
# **Note.** It is guaranteed that there are no students with the same surname 
# at SKILLBEE school.

# Test________________________________________

s1, s2 = input().split(), input().split()
print(*sorted(set(s1) | set(s2)))

#_____________________________________________

# 👨‍🎓 **Online School SKILLBEE 5**
# Every student studying at the online school SKILLBEE studies either history, 
# or literature, or both subjects. The school director has lists of students 
# studying each subject. Accidentally, all student lists got mixed up.
# Write a program that will allow the director to find out how many students 
# study only one subject.
# 
# **Input Format**
# The program receives numbers m and n in the first two lines - the number of 
# students studying history and literature respectively. Then follow m+n lines 
# with surnames of students studying history and literature, in random order.
# 
# **Output Format** 
# The program should output the number of students who study only one subject. 
# If there are no such students, then output `NO`.
# 
# **Note.** It is guaranteed that there are no students with the same surname 
# at SKILLBEE school.

# Test________________________________________
m, n = [int(input()) for _ in range(2)]
object = [input() for _ in range(m)] + [input() for _ in range(n)]
num_students = 0
for i in object:
    if object.count(i) == 1:
        num_students += 1

print(( num_students, "NO")[not num_students])

#_____________________________________________


# 👨‍🎓 **Online School SKILLBEE 6**
# The director of online school SKILLBEE wanted to know which of his students 
# attended all classes since the beginning of the school year. For each class, 
# there is a sheet with a list of students who attended.
# Write a program that determines the surnames of students who attended all classes.
# 
# **Input Format**
# The program receives the number m in the first line - the number of classes 
# held since the beginning of the school year. Then follow m blocks of lines 
# describing sheets with surnames. The first line of each block contains the 
# number of surnames ni, then follow ni lines with surnames of those who 
# attended the i-th class.
# 
# **Output Format** 
# The program should output surnames of students who attended all classes, 
# sorted in lexicographic order. Each surname should be written on a separate line.


# Test________________________________________

num_lesson = int(input())
students = set()

for i in range(num_lesson):
    blocks = set()

    for j in range(int(input())):
        blocks.add(input())
    if students:
        students.intersection_update(blocks)
    else:
        students = blocks

for j in sorted(students):
    print(j)

#_____________________________________________