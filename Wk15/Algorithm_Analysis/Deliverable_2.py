# print_numbers_times_2
def print_numbers_times_2(numbers_list): # 0(n) since there is only one O(n)
	for number in numbers_list: # 0(n)
		print(number * 2) # O(1)
		

# check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b): # O(n^2) since there are two loops within the function.
	for element_a in list_a: # 0(n)
		for element_b in list_b: # 0(n)
			if element_a == element_b: # 0(1)
				return True
				
	return False


# print_10_or_less_elements
def print_10_or_less_elements(list_to_print): # O(1) since the loop is limited to 10 iterations
	list_len = len(list_to_print) # O(1)
	for index in range(min(list_len, 10)): # O(1)
		print(list_to_print[index]) # O(1)
		

# generate_list_trios
def generate_list_trios(list_a, list_b, list_c): # O(n^3) since there are three loops in the function.
	result_list = [] # O(1)
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(n)
			for element_c in list_c: # O(n)
				result_list.append(f'{element_a} {element_b} {element_c}') # O(1)
				
	return result_list 