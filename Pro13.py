"""
Escribe un programa en Python para comprobar si un número es par o impar.
"""

while True:
    numero = input(print("Escribe un numero: "))
    if int(numero) % 2 == 0:
        print("Es par")
    else:
        print("Es impar")