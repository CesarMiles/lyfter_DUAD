int_user_attempt = int(input('Adivine un numero del 1 al 10:'))
import random
int_secret_number = random.randint(1, 10)

while (int_user_attempt != int_secret_number):
    int_user_attempt = int(input('Incorrecto, intenta de nuevo: '))

print('Correcto!')