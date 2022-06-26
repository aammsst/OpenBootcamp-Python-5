# Según la definición de wikipedia, un número primo es
# un número natural (entero) mayor que 1
# que tiene dos divisores positivos distintos: él mismo y el 1.
def esPrimo(num):
    if num <= 1:
        respuesta = "No es un número primo"
    else: 
        for i in range(2,num):
            if num % i == 0:
                respuesta = "No es un número primo"
                break
        else:
            respuesta = "Es un número primo"
    return respuesta

num = int(input("Ingrese un número entero: "))
print(esPrimo(num))
