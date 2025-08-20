def print_message(msg):
    print(f"Detalle importante: {msg}")


def print_summary():
    print_message("Este es el resumen ejecutivo")
    print("-- Fin del reporte --")


print_message("Inicio del programa")
print_summary()