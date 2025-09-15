#Function for sorting list using 'bubbles_sort' algorithm
def bubble_sort(list_to_sort):
  for outer_index in range(len(list_to_sort)-1):
    has_made_changes = False
    inner_counter = 0
    for index in range(len(list_to_sort)-1, outer_index, -1):
      current_element = list_to_sort[index]
      next_element = list_to_sort[index - 1]
      print(f'Iteration {outer_index}.{inner_counter}. Current element {current_element}, next element {next_element}')
      inner_counter += 1

      if next_element > current_element:
        print(f'{next_element} is greater than {current_element} \n'
              f'Switching position {current_element} with {next_element}')
        list_to_sort[index] = next_element
        list_to_sort[index - 1] = current_element
        has_made_changes = True
    
    if not has_made_changes:
      return


# Testing Section 
my_test_list = [5,8,3,1]
print(my_test_list)
bubble_sort(my_test_list)

print(my_test_list)