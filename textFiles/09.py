"""🔍⏱️ Log File Analysis
You are given a text file logfile.txt containing login and logout times of users. Each line has three comma-separated values:
username, login_time, logout_time (in 24-hour format).

Write a program that creates output.txt and writes the names of all users (in original order) who were online for at least one hour.

Key Requirements:
Parse each line: username, HH:MM, HH:MM
Calculate session duration: logout_time - login_time
Filter users: duration >= 60 minutes
Preserve original order of appearance in input file
Example Input Line:
john_doe, 09:30, 10:45 → Duration=75 minutes → Included
jane_smith, 14:00, 14:45 → Duration=45 minutes → Excluded"""


with open("logfile.txt", "r", encoding="UTF-8") as first_file, open("output.txt", "w", encoding="UTF-8") as new_file:
    l2 = []

    for line in first_file:
        l = line.split(", ")
        came_time = l[-2].strip().replace(":", ".")
        left_time = l[-1].strip().replace(":", ".")
        if float(left_time) - float(came_time) >= 1:
            l2 += [l[0]]
    new_file.write("\n".join(l2))
