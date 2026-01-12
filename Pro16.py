"""
Escriba un programa en Python para encontrar el factorial de un número.

Para encontrar el factorial de un número entero positivo (\(n!\)),
debes multiplicar ese número por todos los números enteros positivos menores que él hasta llegar a 1
Ejemplo: 5! = 5x4x3x2x1 = 120
"""

while True:
    numero = int(input("Escriba un numero para encontrar su factorial: "))
    if numero == 0:
        print('Factorial es igual a 0')
        break
    else:
        contador = 1
        for i in range(1, numero + 1):
            contador *= i
            print(contador)
        print('Factorial es igual a {}'.format(contador))