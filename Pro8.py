"""
Write a Python program to display calendar.
"""

import calendar

year = int(input('Ingrese el año: '))
month = int(input('Ingrese el mes: '))

calendario = calendar.month(year, month)
print(calendario)