# cálculo del área de un triángulo
# suponiendo triángulo rectángulo con ángulo recto en la base

def areaTriangulo(altura = 0, base = 0):
    resultado = altura * base * 0.5
    return resultado

# área de un círculo
def areaCirculo(radio = 0):
    resultado = 3.1415 * radio**2
    return resultado

# ingreso de datos e impresión de área del triángulo
altura = int(input("Ingrese altura del triángulo: "))
base = int(input("Ingrese base del triángulo: "))
print("El área del triángulo es:", areaTriangulo(altura, base))

# ingreso de datos e impresión de área del círculo 
radio = int(input("\nIngrese radio del círculo: "))
print("El área del círculo es:", areaCirculo(radio))
