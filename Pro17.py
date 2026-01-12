"""
Write a Python Program to Display the multiplication Table.
"""

tabla = int(input("Escriba un numero para desplegar tabla de multiplicar: "))

for i in range(1,11):
    print(f'{tabla} * {i} = {tabla * i}')