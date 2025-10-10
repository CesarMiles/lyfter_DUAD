def list_summarization(numbers_to_sum):
    result = 0
    for numbers in numbers_to_sum:
        result += numbers
    return result 


my_list = [1, 2, 4]
list_summarization(my_list)
print(list_summarization(my_list))