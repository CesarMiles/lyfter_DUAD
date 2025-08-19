lista_de_num = []
for i in range(3):
    numeros = int(input(f'{i+1}. Ingrese un numero: '))
    lista_de_num.append(numeros)

if(lista_de_num[0]== 30 or lista_de_num[1]== 30 or lista_de_num[2]== 30):
    print ('Correcto!')
elif (lista_de_num[0] + lista_de_num[1] + lista_de_num[2] == 30):
    print ('Correcto!')
else:
    print('Incorrecto')
