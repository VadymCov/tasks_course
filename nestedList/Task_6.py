#  🪐 Chunking Into Pieces
#  Two input lines are given: the first is a sequence of characters, the second is a number n.
#  From the first line, form a list.
#
#  Implement a function chunked() that takes a list and a chunk-size number,
#  and returns a list of chunks of that size.
#
#  Input format:
#  Two lines are given to the program: a text string of characters separated by space,
#  and a number n on a separate line.


def chunked(row, n):

    result = []

    while len(row) > 0:

        res = []

        for i in range(n):
            if len(row) == 0:
                break
            tmp = row.pop(i - i)
            res.append(tmp)

        result.append(res)
        
    return result


# Test _______________
row = input().split()
n = int(input())

print(chunked(row, n))
