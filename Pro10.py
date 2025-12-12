"""
Write a Python program to swap two variables without temp variable.
"""

a = int(input('Ingrese valor a: '))
b = int(input('Ingrese valor b: '))

print(f'Valores ingresados para a: {a} y b: {b}')

# swap de variables
a, b = b, a

print(f'Valores despues del swap para a: {a} y b: {b}')
