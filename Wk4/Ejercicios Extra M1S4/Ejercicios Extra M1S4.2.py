tiempo = int(input("Ingrese el tiempo en segundos: "))
diez_min_en_seg = 600
if (tiempo < diez_min_en_seg):
    resultado = diez_min_en_seg - tiempo
elif (tiempo == diez_min_en_seg):
    resultado = "Igual"
else:
    resultado = "Mayor"
print(resultado)
