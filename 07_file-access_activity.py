# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:53:07 2019

@author: CEC
"""

file=open("devices.txt","a")
while True:
    print("\n Escriba exit para salir")
    newItem=input("Ingrese el nuevo dispositivo: ")
    
    if newItem.lower()=="exit":
        
        print("Terminado")
        break
    file.write(newItem+"\n")
    
file.close
file=open("devices.txt","r")
print(file.read())
file.close
