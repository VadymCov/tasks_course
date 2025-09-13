# 🔢 Number Memory Tracker 🧠
# 
# A sequence analyzer needs to check if each number in a stream has appeared before.
# The system keeps track of previously seen numbers and reports duplicates as they occur,
# ignoring leading zeros in number formatting.
#
# Input:
#   A single line of text containing numbers separated by spaces.
#
# Output:
#   For each number, print "YES" (on a separate line) if this number has appeared 
#   earlier in the sequence, or "NO" otherwise.
#
# Note: Leading zeros in numbers should be ignored.



# Test_1___________________________________

s = input().split()
compare = set()

for i in s:
    if int(i) not in compare:
        print("NO")
        compare.add(int(i))
    else:
        print("YES")

# Test_2____________________________________

clean_string = [int(i) for i in input().split()]
compare = set()

for i in clean_string:
    if i in compare:
        print('YES')
    else:
        print('NO')
        compare.add(i)

# Test_3____________________________________

s = set()
for i in input().split():
    print(['NO', 'YES'][i in s])
    s.add(i)