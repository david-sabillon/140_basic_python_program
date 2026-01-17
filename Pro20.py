"""
Write a Python Program to Find Armstrong Number in an Interval.
"""

menor = int(input('Ingrese el primer numero del intervalo: '))
mayor = int(input('Ingrese el ultimo numero del intervalo: '))

def armstrong_number(numero):
    # Calcular el numero de digitos convirtiendo a string
    iterable = (str(numero))
    exponente = len(iterable)

    # Iterar cada valor y elevando al exponente
    resultado = 0
    for i in iterable:
        resultado += int(i) ** exponente

    # Comparar para si es el resultado es igual al numero ingresado
    return resultado if numero == resultado else False

for n in range(menor, mayor + 1):
    if numero_encontrado := armstrong_number(n):
        print(f"{numero_encontrado} es un numero Armstrong.")