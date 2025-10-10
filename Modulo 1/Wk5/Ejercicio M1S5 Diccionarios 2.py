list_key = []
list_value = []
dictionary = {}
dictionary_size = int(input('Ingrese el tamaño de su diccionario: '))
while (dictionary_size > 0):
     key = input('Ingrese su key: ')
     value = input('Ingrese su value: ')
     list_key.append(key)
     list_value.append(value)
     dictionary [key] = value
     dictionary_size += -1

print(list_key)
print(list_value)
print(dictionary)