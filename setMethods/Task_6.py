# 📊 Tracking the success of the solution
#
# An online learning platform should track the progress of students in solving programming problems.
# The system counts the number of students who solved the problem correctly and calculates the
# success rate of all attempts, providing motivating feedback.
#
# Input:
# The first line contains an integer n — the total number of solution attempts.
# Then n lines represent the students' solutions in the format:
# <nickname>: <check_system_result>
# where <check_system_result> can be "Correct" or "Incorrect".
#
# Output:
# If there are correct solutions:
# "<number_of_correct_students> students solved correctly"
# "Of all regions, <percentage_of_correct>% correct"
# If there are no correct solutions:
# "You can be the first to solve this problem"
#
# Note 1: Mathematical rounding rules apply - round to the nearest whole number.
# Note 2: Student nicknames are guaranteed to be unique.
# Note 3: Nicknames cannot contain a colon (:).


from math import ceil, floor

def correct_decisions_counter(n, all_solution):
    keyword = ["correct", "Вы можете стать первым, кто решит эту задачу"] 

    if n < 1:
        return keyword[1]

    my_s = set()

    cnt_sel = 0
    cnt_all = 0

    for i in all_solution:
        if keyword[0] in i:
            cnt_all += 1
        if keyword[0] in i and i not in my_s:
            my_s.add(i)
            cnt_sel += 1

    percentage_of_completion = cnt_all / n * 100

    if cnt_sel > 0:
        if percentage_of_completion % 1 < 0.5:
            percentage_of_completion = floor(percentage_of_completion)
        else:
            percentage_of_completion = ceil(percentage_of_completion)


        return(f"Верно решили {cnt_sel} учащихся\n"
            f"Из всех попыток {percentage_of_completion}% верных")
    else:
        return keyword[1]



# Test______________________________________________

n = int(input())
all_solution = [input().lower() for _ in  range(n)]

print(correct_decisions_counter(n, all_solution))