#Function for sorting list using 'bubbles_sort' algorithm
def bubble_sort(list_to_sort):
  for outer_index in range(0, len(list_to_sort)-1):
    has_made_changes = False
    for index in range(0, len(list_to_sort)-1 -outer_index):
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]
      print(f'Iteration {outer_index}.{index}. Current element {current_element}, next element {next_element}')

      if current_element > next_element:
        print(f'{current_element} is greater than {next_element} \n'
              f'Switching position {next_element} with {current_element}')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True
    
    if not has_made_changes:
      return







# def bubble_sort(list_to_sort):
#   for outer_index in range(0, len(list_to_sort) -1):
#     has_made_changes = False
#     for index in range(0, len(list_to_sort)-1 -outer_index):
#         # Guardamos los valores del elemento actual y el siguiente
#         current_element = list_to_sort[index]
#         next_element = list_to_sort[index + 1]

#         print(f'-- Iteracion {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

#         if current_element > next_element:
#             print(f'El elemento actual es mayor al siguiente. Intercambiando {current_element} por {next_element}')
#             list_to_sort[index] = next_element
#             list_to_sort[index + 1] = current_element
#             has_made_changes = True
#     if not has_made_changes:
#        return


my_test_list = [-3, 5, 6, 18]
print(my_test_list)
bubble_sort(my_test_list)

print(my_test_list)