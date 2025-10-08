# 🔒 Good Password
# A good password per this task consists of at least 7 characters,
# contains at least one digit, one uppercase and one lowercase letter.
# Write a program using the built-in any() function to check if the entered password is good.

# Input Format: One line of text.

# Output Format: YES if the string is a good password, NO otherwise.

pass_str = input()
result = all(
    [
        any(map(lambda x: x.isdigit(), pass_str)),
        any(map(lambda x: x.isupper(), pass_str)),
        any(map(lambda x: x.islower(), pass_str)),
        len(pass_str) >= 7
        ]
    )
print(("NO", "YES")[result])