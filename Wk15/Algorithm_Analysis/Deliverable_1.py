#Function for sorting list using 'bubbles_sort' algorithm
def bubble_sort(list_to_sort): # O(n^2) since there are two loops within the function.
  for outer_index in range(0, len(list_to_sort)-1): # O(n)
    has_made_changes = False # O(1)
    for index in range(0, len(list_to_sort)-1 -outer_index): # O(n) 
      current_element = list_to_sort[index] # O(1)
      next_element = list_to_sort[index + 1] # O(1)
      print(f'Iteration {outer_index}.{index}. Current element {current_element}, next element {next_element}') # O(1)

      if current_element > next_element: # O(1)
        print(f'{current_element} is greater than {next_element} \n' 
              f'Switching position {next_element} with {current_element}') # O(1)
        list_to_sort[index] = next_element # O(1)
        list_to_sort[index + 1] = current_element # O(1)
        has_made_changes = True # O(1)
    
    if not has_made_changes: # O(1)
      return


# Testing Section 
my_test_list = [-3, 5, 6, 18]
print(my_test_list)
bubble_sort(my_test_list)

print(my_test_list)