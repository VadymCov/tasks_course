# 😈 **Dangerous Virus**
# A dangerous virus has infiltrated the file system of the computer where our 
# platform is deployed and broke the file access control. They say the virus 
# was written by one of the students from the Python for beginners course.
# For each file it is known what actions can be performed on it:
# * write W (write access to the file);
# * read R (read access from the file);
# * execute X (execute access to run the file).
# Write a program to restore file access control. Your program should return 
# `OK` for each request if a valid operation is performed, and `Access denied` 
# if the operation is invalid.
# 
# **Input Format**
# The program receives the number of files n contained in the computer's file system. 
# Then follow n lines, each containing a file name and allowed operations with it, 
# separated by a space. The next line contains the number m - the number of file 
# requests, and then m lines with requests in the format `operation file`. 
# Any number of requests can be addressed to the same file.
# 
# **Output Format** 
# The program should output for each of the m requests on a separate line 
# `Access denied` or `OK`.

# Test________________________________________________

operation_map = {
    "read": "R",
    "write": "W",
    "execute": "X"
}

n = int(input())

file_permissions = {}

for _ in range(n):
    line = input().split()
    filename = line[0]
    permissions = line[1:]
    file_permissions[filename] = permissions

m = int(input())

for _ in range(m):
    operation, filename = input().split()
    operation_litter = operation_map[operation]
    if filename in file_permissions and operation_litter in file_permissions[filename]:
        print("OK")
    else:
        print("Access denied")