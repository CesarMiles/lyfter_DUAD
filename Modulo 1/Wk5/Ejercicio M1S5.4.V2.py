my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 11, 11, 11, 11]

for numbers in range(len(my_list)-1, -1, -1):
    if my_list[numbers] % 2 == 1:
        my_list.pop(numbers)


print(my_list)