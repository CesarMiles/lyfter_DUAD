full_name = input('Ingrese su nombre y apellido: ')
user_age = int(input('Ingrese su edad: '))

if (user_age < 3):
    print (f'{full_name} es un bebe')
elif (user_age < 11):
    print (f'{full_name} es un niño')
elif (user_age < 15):
    print (f'{full_name} es un preadolescente')
elif (user_age < 18):
    print (f'{full_name} es un adolescente')
elif (user_age < 21):
    print (f'{full_name} es un adulto jovan')
elif (user_age < 65):
    print (f'{full_name} es un adulto')
else:
    print(f'{full_name} es un adulto mayor')