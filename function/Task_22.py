"""Your task is to count how many numbers are between [a,b] each number is 2 is 5 For example,
 between [1,100] there are 2 , 5 , 22 , 25 , 52 and 55 , so the answer is 6"""

def count_numbers(a, b):
    counter = 0
    list_temp = [2, 5]
    while list_temp:
        n = list_temp.pop(0)

        if a <= n <= b:
            counter += 1
        new_temp_2 = n * 10 + 2
        new_temp_5 = n * 10 + 5

        if new_temp_2 <= b:
            list_temp.append(new_temp_2)

        if new_temp_5 <= b:
            list_temp.append(new_temp_5)
    return counter

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512