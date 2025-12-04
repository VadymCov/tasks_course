# 📚 Top Students
# Teacher Alice was checking math tests in several classes of the online school ByteCamp and
# decided to verify that each class has at least one top student – a pupil with a grade of 5 on the test.
# Write a program using the built-in functions all() and any() to help Alice with the check.

# Input Format
# The input starts with a natural number n – the number of classes. Then, for each class, a block of information is provided:

# a natural number k – the number of students in the class;
# followed by k lines in the format: surname grade.

# Output Format
# Output YES if each class has at least one top student, and NO otherwise.

my_list2 = []
for i in range(int(input())):
    my_list = []
    for j in range(int(input())):
        cls_num = list(map(lambda x: "5" in x, input().split()))
        my_list += cls_num
    my_list2.append(any(my_list))
if all(my_list2):
    print("YES")
else:
    print("NO")
