counter = 0 
list = []
while counter != 10:
    list.append(int(input('Ingrese un numero: ')))
    counter += 1

greater_number = list[0]  
for number in list:       
    if number > greater_number:
        greater_number = number
print(f'{list}. El mas alto fue {greater_number}')