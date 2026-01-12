"""
Escriba un programa en Python para verificar si un año es bisiesto.
"""

while True:

    year = int(input(print("Escribe un año para verificar si es bisiesto: ")))
    if year % 100 == 0:
        print(f"{year} no es bisiesto")
    elif year % 100 and year % 400 == 0: # Excepcion de la excepcion
        print(f"{year} es bisiesto")
    elif year % 4 == 0:
        print(f"{year} es bisiesto")
    else:
        print(f"{year} no es bisiesto")
