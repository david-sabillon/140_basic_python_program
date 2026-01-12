"""
Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

Números primos:
Un número primo es un número entero que no puede dividirse exactamente por ningún otro número,
excepto por el 1 y por sí mismo. Por ejemplo, 2, 3, 5, 7, 11 y 13 son números primos porque
no pueden dividirse por ningún otro número entero positivo excepto por el 1 y su propio valor.
"""


while True:
    numero = int(input("Escriba un numero para verificar si es primo: "))
    flag = False
    if numero <= 1:
        print(f"{numero} Numero menor o igual a 1. No es primo")
    elif numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                flag = True
                break
    if flag:
        print(f"{numero} No es primo")
    else:
        print(f"{numero} es primo")