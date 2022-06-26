def esAñoBisiesto(año):
    # condición de año bisiesto, sacado de internet
    condicion = ((año % 4 == 0) and (año % 100 != 0) or año % 400 == 0)
    respuesta = "Es un año bisiesto." if condicion else "No es un año bisiesto"
    return respuesta

año = int(input("Ingrese un año: "))
print(esAñoBisiesto(año))
