"""
Write a Python Program to Find HCF.

Máximo Común Divisor (MCD):
El MCD, o Máximo Común Divisor, es el mayor entero positivo que divide dos o más números sin dejar residuo.
Fórmula:
Para dos números a y b, el MCD se puede calcular mediante la fórmula:
HCF(𝑎,𝑏) = GCD(𝑎,𝑏)

Para más de dos números, se puede calcular el MCD calculando el MCD de pares de números a la vez hasta llegar al
último par.
Nota: MCD significa Máximo Común Divisor.
"""

def calcular_mcd(x, y):
    hcf = None
    menor = num1 if num1 <= num2 else num2
    for i in range(1, menor + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

print(f"El MCD es: {calcular_mcd(num1, num2)}")