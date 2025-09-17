# 👨‍💻 **Computer Science Lesson**
# Given grades on a 10-point scale in computer science for three students. Write a program 
# that outputs the set of grades that both the first and second students have, 
# but the third student does not have.
# 
# **Input Format**
# The program receives grades of three students, separated by spaces 
# (each student's grades on a separate line).
# 
# **Output Format** 
# The program should output the set of grades **in descending order** on one line, 
# separated by spaces, according to the task condition.
# 
# **Note.** A student's grade is in the range from 0 to 10 inclusive.

# Test _______________________________________________

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = set(map(int, input().split()))

result = (s1.intersection(s2)) - s3

print(*sorted(result, reverse=True))

#_____________________________________________________



# 🧠 **Math Lesson**
# Given math grades for three students on a 10-point scale. Write a program 
# that outputs grades that appear in no more than two students.
# 
# **Input Format**
# The program receives grades of three students, separated by spaces 
# (each student's grades on a separate line).
# 
# **Output Format** 
# The program should output the set of grades **in ascending order** on one line, 
# separated by spaces, according to the task condition.


# Test______________________________________________

stud1 = set(map(int, input().split()))
stud2 = set(map(int, input().split()))
stud3 = set(map(int, input().split()))

int_section = stud1 & stud2 & stud3
all_set = stud1 | stud2 | stud3

for i in int_section:
    all_set.remove(i)
print(*all_set)

#___________________________________________________


# 🧲 **Physics Lesson**
# Given physics grades for three students on a 10-point scale. Write a program 
# that outputs the set of grades of the third student that do not appear 
# in either the first or second student.
# 
# **Input Format**
# The program receives grades of three students, separated by spaces 
# (each student's grades on a separate line).
# 
# **Output Format** 
# The program should output the set of grades **in descending order** on one line, 
# separated by spaces, according to the task condition.
# 
# **Note.** A student's grade is in the range from 0 to 10 inclusive.


# Test______________________________________________

s1 = set([int(i) for i in input().split()])
s2 = set([int(i) for i in input().split()])
s3 = set([int(i) for i in input().split()])

result = s3 - (s1 | s2)
print(*sorted(result, reverse=True))
#___________________________________________________


# 🌱 **Biology Lesson**
# Given biology grades for three students on a 10-point scale. Write a program 
# that outputs the set of grades that do not appear in any of the three students.
# 
# **Input Format**
# The program receives grades of three students, separated by spaces 
# (each student's grades on a separate line).
# 
# **Output Format** 
# The program should output the set of grades **in ascending order** on one line, 
# separated by spaces, according to the task condition.
# 
# **Note.** A student's grade is in the range from 0 to 10 inclusive.

# Test ____________________________________________
s1 = {int(i) for i in input().split()}
s2 = {int(i) for i in input().split()}
s3 = {int(i) for i in input().split()}

print(*sorted(set(range(10 + 1)) - s1.union(s2,s3)))
#__________________________________________________