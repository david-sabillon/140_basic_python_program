"""
Write a Python Program to Check Armstrong Number?

Número de Armstrong:
Es un número que es igual a la suma de sus propios dígitos, cada uno elevado a una potencia igual al número de dígitos
que tiene dicho número.

Por ejemplo, consideremos el número 153:Tiene tres dígitos (1, 5 y 3).Si calculamos \(1^{3}+5^{3}+3^{3}\), obtenemos
\(1+125+27\), que es igual a 153. Por lo tanto, 153 es un número de Armstrong porque equivale a la suma de sus dígitos
elevados a la potencia del número total de sus dígitos.

Otro ejemplo es el 9474:Tiene cuatro dígitos (9, 4, 7 y 4).Si calculamos \(9^{4}+4^{4}+7^{4}+4^{4}\), obtenemos
\(6561+256+2401+256\), que también es igual a 9474.Por lo tanto, 9474 también es un número de Armstrong
"""

numero = int(input('Ingrese un numero para comprobar si es un numero Armstrong: '))

# Calcular el numero de digitos convirtiendo a string
iterable = (str(numero))
exponente = len(iterable)

# Iterar cada valor y elevando al exponente
resultado = 0
for i in iterable:
    resultado += int(i) ** exponente

# Comparar para si es el resultado es igual al numero ingresado
aplicacion = f"{numero} es número de Armstrong" if numero == resultado else f"{numero} no es número de Armstrong"
print(aplicacion)





