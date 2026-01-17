"""
Write a Python Program to Find the Sum of Natural Numbers.

Los números naturales son un conjunto de enteros positivos que se utilizan para contar y ordenar objetos.
Son los números que suelen empezar en 1 y continuar indefinidamente, incluyendo todos los números enteros mayores que 0.
En notación matemática, el conjunto de números naturales suele denotarse como "N" y puede expresarse como:
𝑁 = 1, 2, 3, 4, 5, 6, 7, 8,...
"""

num_intervalo = int(input('Ingrese el numero para realizar la suma del intervalo: '))

acumulador = 0
while num_intervalo != 0:
    acumulador += num_intervalo
    num_intervalo -= 1
print(f"La suma de los números naturales es: {acumulador}")

