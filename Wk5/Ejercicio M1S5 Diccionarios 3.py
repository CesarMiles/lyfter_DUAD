employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
list_of_keys_to_delete = []
print(f' Este es el direccionario actual {employee}')
modify_confirmation = input('Si desea modificar este diccionario ingrese Yes: ')
while modify_confirmation == 'Yes' or modify_confirmation == 'yes':
    keys_to_delete = input('Ingrese los keys a eliminar: ')
    list_of_keys_to_delete.append(keys_to_delete)
    modify_confirmation = input('Si desea continuar ingrese Yes: ')

for key in range(0, len(list_of_keys_to_delete)):
    employee.pop(list_of_keys_to_delete[key])


print(f' keys eliminados  {list_of_keys_to_delete}')
print(f'Estes el nuevo diccionario {employee}')



