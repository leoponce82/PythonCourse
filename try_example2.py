# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:34:06 2019

@author: CEC
"""

try:
    x=int(input("Ingrese valor: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No se puede dividir para 0")
except ArithmeticError: #Solo sale si se escribe antes que la condicion de Zero division. Porq es mas general que la zeroDivision
    print("Problema aritmetico")
except ValueError:
    print("Debe ser un entero")
except: 
    print("No se que pero algo salio mal")
print("Fin")