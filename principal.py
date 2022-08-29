import rombo
import circulo
import triangulo
import trapecio
import cubo
import esfera

print("Menu de operaciones")
print("1. área de un rombo")
print("2. área de un circulo")
print("3. área de un triangulo teorema de herón")
print("4. área de un trapecio")
print("5. volumen de un cubo")
print("6. area de una esfera")

opc = input("Escoja opcion")

if (opc == 1):
    calcular_area_rombo()
elif (opc == 2):
    calcular_area_circulo()
elif (opc == 3):
    calcular_area_triangulo()
elif (opc == 4):
    calcular_area_trapecio()
elif (opc == 5):
    calcular_volumen_cubo()
elif (opc == 6):
    calcular_area_esfera()
else:
    print("Opcion no valida")
