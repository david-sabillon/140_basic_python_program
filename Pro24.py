"""
Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

¿Cómo podemos convertir manualmente un número decimal a binario, octal y hexadecimal?
Convertir un número decimal a binario, octal y hexadecimal implica dividir el número decimal por la base repetidamente
y anotar los residuos en cada paso. Aquí tienes un ejemplo sencillo:
Convirtamos el número decimal 27 a binario, octal y hexadecimal.

1. Binario:
Dividir 27 entre 2. El cociente es 13, el residuo es 1. Anotar el residuo.
Dividir 13 entre 2. El cociente es 6, el residuo es 1. Anotar el residuo.
Dividir 6 entre 2. El cociente es 3, el residuo es 0. Anotar el residuo.
Dividir 3 entre 2. El cociente es 1, el residuo es 1. Anotar el residuo.
Dividir 1 entre 2. El cociente es 0, el residuo es 1. Anotar el residuo.
Leyendo los restos de abajo hacia arriba, la representación binaria de 27 es 11011

2. Octal
Dividir 27 entre 8. El cociente es 3, el resto es 3. Anote el resto.
Dividir 3 entre 8. El cociente es 0, el resto es 3. Anote el resto.
Leyendo los restos de abajo a arriba, la representación octal de 27 es 33.

3. Hexadecimal
Dividir 27 entre 16. El cociente es 1, el residuo es 11 (B en hexadecimal). Observe el residuo.
Al leer los residuos, la representación hexadecimal de 27 es 1B.
En resumen:
Binario: 27 en decimal es 11011 en binario.
Octal: 27 en decimal es 33 en octal.
Hexadecimal: 27 en decimal es 1B en hexadecimal.
"""

import math

def binaro(nu):
    dividendo = nu
    residuo = []
    while dividendo > 0:
        if dividendo % 2 == 0:
            residuo.append(0)
        else:
            residuo.append(1)
        dividendo = math.floor(dividendo / 2)
    resultado = "".join(map(str, residuo[::-1]))
    return resultado

def octal(nume):
    dividendo = nume
    residuo = []
    while dividendo > 0:
        residuo.append(round(dividendo / 8 - (dividendo := math.floor(dividendo / 8)), 2))
    resultado = [int(str(v).split(".")[1][0]) for v in residuo[::-1]]
    resultado = "".join(map(str, resultado))
    return resultado

def hexadecimal(numero):
    dividendo = numero
    valores = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    encontrado = []

    while dividendo > 0:
        residuo = dividendo - (16 * (math.floor(dividendo / 16)))
        dividendo = math.floor(dividendo / 16)
        encontrado.append(valores[residuo])
    resultado = "".join(map(str, encontrado[::-1]))
    return resultado

num = int(input('Ingrese el numero para encontrar sus variables: '))
print(f"El binario de {num} es: {binaro(num)}")
print(f"El octal de {num} es: {octal(num)}")
print(f"El hexadecimal de {num} es: {hexadecimal(num)}")