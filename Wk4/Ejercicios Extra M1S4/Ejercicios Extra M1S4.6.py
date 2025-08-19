num = int(input("Ingrese un número: "))
for contador in range(1, 13):
    res = num * contador
    print(f'{num} x {contador} = {res}')
    contador + 1
