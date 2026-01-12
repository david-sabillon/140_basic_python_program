"""
Escriba un programa en Python para imprimir todos los números primos en un intervalo de 1 a 10

Números primos:
Un número primo es un número entero que no puede dividirse exactamente por ningún otro número,
excepto por el 1 y por sí mismo. Por ejemplo, 2, 3, 5, 7, 11 y 13 son números primos porque
no pueden dividirse por ningún otro número entero positivo excepto por el 1 y su propio valor.
"""

for i in range(2,100):
    flag = False
    for n in range(2,i):
        if i % n == 0 or i == 1:
            flag = True
            break
        else:
            flag = False
    if not flag:
        print(i)
