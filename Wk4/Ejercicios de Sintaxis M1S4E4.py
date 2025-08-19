lista_numeros = []
for i in range(3):
    numero = int(input(f'{i+1}. Ingrese un numero: '))
    lista_numeros.append(numero)

if (lista_numeros[0]> lista_numeros[1] and lista_numeros[0]>lista_numeros[2]):
    print (lista_numeros[0])
elif (lista_numeros[1]> lista_numeros[0] and lista_numeros[1]>lista_numeros[2]):
        print (lista_numeros[1])
elif (lista_numeros[2]> lista_numeros[0] and lista_numeros[2]>lista_numeros[1]):
        print (lista_numeros[2])
