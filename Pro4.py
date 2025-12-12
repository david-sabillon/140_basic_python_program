"""
Escribe un programa en Python para intercambiar dos variables.
"""

valor_a = input("Enter the value of the first variable (a): ")
valor_b = input("Enter the value of the second variable (b): ")
valor_c = None

print(f'valores antes del swap: a = {valor_a}, b = {valor_b}')
valor_c = valor_a; valor_a = valor_b; valor_b = valor_c
print(f'valores despues del swap: a = {valor_a}, b = {valor_b}')