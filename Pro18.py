"""
Write a Python Program to Print the Fibonacci sequence.

Fibonacci sequence:
La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores,
comenzando típicamente con 0 y 1. Por lo tanto, la secuencia comienza con 0 y 1, y el siguiente número
se obtiene sumando los dos anteriores. Este patrón continúa indefinidamente, generando una secuencia
similar a la siguiente:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Matemáticamente, la secuencia de Fibonacci se puede definir mediante la siguiente relación de recurrencia:
𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1
"""

secuencia = int(input('Defina el numero para el tamano de la secuencia: '))
primero = 0
segundo = 1
contador = 1

print('Secuencia Finobacci:')
while contador < secuencia:
    resultado = primero + segundo
    if primero == 0: print(primero)
    print(resultado)
    primero = segundo
    segundo = resultado
    contador += 1
