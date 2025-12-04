# 🎓 **Course Information System**
# Write a program that outputs information about a given course by course number.
# 
# Course Number (key) | Auditorium Number (value) | Instructor (value) | Time (value)
# CS101               | 3004                      | Hayes              | 8:00
# CS102               | 4501                      | Alvarado           | 9:00
# CS103               | 6755                      | Rich               | 10:00
# NT110               | 1244                      | Burke              | 11:00
# CM241               | 1411                      | Lee                | 13:00
# 
# **Input Format**
# The program receives one line - a course number.
# 
# **Output Format** 
# The program should output the course number, then the auditorium number, 
# instructor name and course time according to the examples.
# 
# **Note 1.** Use a dictionary instead of conditional operators.
# 
# **Note 2.** For convenient output, use the format() method or f-strings.

# Test _______________________________________________________

dictionary = {
    'CS101':	('3004', 'Хайнс', '8:00'),
    'CS102':	('4501', 'Альварадо', '9:00'),
    'CS103':	('6755', 'Рич', '10:00'),
    'NT110':	('1244', 'Берк', '11:00'),
    'CM241':	('1411', 'Ли', '13:00')
}

num_course = input()
room, teacher, time = dictionary[num_course]

print(f"{num_course}: {room}, {teacher}, {time}")
