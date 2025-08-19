precio_de_producto = int(input("Ingrese el precio del producto: "))
if(precio_de_producto < 100):
    descuento = precio_de_producto * 0.02
else:
    descuento = precio_de_producto * 0.1
precio_final = precio_de_producto - descuento
print (precio_final)
