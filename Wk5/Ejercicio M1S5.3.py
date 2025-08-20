my_list = [10, 4, 3, 6, 1, 7, 10, 5, 23]

first_list_item = my_list.pop(0)
last_list_item = my_list.pop(len(my_list)-1)
my_list.insert(0, last_list_item) 
my_list.insert(len(my_list), first_list_item) 

print(my_list)