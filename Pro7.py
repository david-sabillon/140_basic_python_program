"""
Write a Python program to convert Celsius to Fahrenheit. F = (C * 9/5) + 32
"""

celsius = float(input('Ingrese la cantidad de grados Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'La conversion de los grados Celsius ingresados equivale a {fahrenheit:.2f} grados Fahrenheit')