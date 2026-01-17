"""
Write a Python Program To Find ASCII value of a character.

ASCII, o Código Estándar Americano para el Intercambio de Información, es un estándar de codificación de caracteres que
utiliza valores numéricos para representar caracteres. A cada carácter ASCII se le asigna un número binario único de 7
u 8 bits, lo que permite a las computadoras intercambiar información y mostrar texto de forma coherente.
Los valores ASCII van de 0 a 127 (para ASCII de 7 bits) o de 0 a 255 (para ASCII de 8 bits), y cada valor corresponde a
un carácter específico, como letras, dígitos, signos de puntuación y caracteres de control.
"""

while True:
    caracter = str(input('Escriba un caracter para encontrar el codigo ASCII: '))
    print(f"El codigo ASCII de {caracter} es: ", ord(caracter))

