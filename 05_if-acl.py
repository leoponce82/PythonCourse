# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:28:45 2019

@author: CEC
"""

num=int(input("Ingrese un numero entre 0 y 100:"))
if num<0:
    print("numero invalido menor a 0")
elif num>100:
    print("numero invalido mayor a 100")
else:
    print("numero valido "+str(num))
    
    
#loop for
lista=["r1","r2","r3","s4","s5","s6"]
for nums in lista:
    print(nums)
###############################
for nums in lista:
    if "s" in nums:
        print(nums)
##############################
lista2=[]
for nums in lista:
    if "s" in nums:
        lista2.append(nums)#ASI SE agrega datos que cumplan con un IF a una nueva lista
lista2
        
    