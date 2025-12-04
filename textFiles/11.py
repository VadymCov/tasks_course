"""🔍📝 Missing Docstrings
You are given a Python code file.
Find all function definitions (lines starting with def ) that lack a comment (#) in the immediate previous line.

Requirements:
Input: Filename of a Python source file
Function detection: Any line starting with def
Comment check: Examine the line immediately above the function definition
Must start with # to count as valid documentation
Output:
Names of undocumented functions (in order of appearance), each on a new line
If all functions are documented: Best Programming Team
"""
with open(input(), "r", encoding="UTF-8") as f:
    lines = f.readlines()
    list_result = []

    for i in range(len(lines)):
        if lines[i].startswith("def "):
            if i == 0 or not lines[i - 1].strip().startswith("#"):
                last_inx = lines[i].find("(")
                list_result.append(lines[i][4:last_inx].strip())

    print("\n".join(list_result) if list_result else "Best Programming Team")