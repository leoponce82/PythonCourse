# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:32:43 2019

@author: CEC ponce
"""

num=int(input("Ingrese un numero: "))

if abs(num)%2>0:
    print("numero es impar")
elif num==0:
    print("numero es cero") 
elif abs(num)%2==0:
    print("numero es par")

   
