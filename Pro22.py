"""
Write a Python Program to Find LCM.

Mínimo Común Múltiplo (MCM):
El MCM, o Mínimo Común Múltiplo, es el múltiplo más pequeño que es exactamente divisible entre dos o más números.
Fórmula:
Para dos números a y b, el MCM se puede calcular mediante la fórmula:
|𝑎 ⋅ 𝑏|
MCM(𝑎,𝑏) = MCD(𝑎,𝑏)
Para más de dos números, se puede calcular el MCM paso a paso, calculando el MCM de pares de números a la vez hasta
llegar al último par.
Nota: MCD significa Máximo Común Divisor.
"""

def calcular_mcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

print("El MCM es: ", calcular_mcm(num1, num2))
