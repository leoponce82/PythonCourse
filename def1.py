# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:18:54 2019

@author: CEC
"""



def hi(name1,name2):
    print("Hi ", name1)
    print("Hi ", name2)

hi("Leo","Vel")
###############################################################
def address(calle,ciudad,postal):
    print("Su direccion: ", calle, ciudad, postal)
s=input("Calle: ")
pc=input("Cofigo postal: ")
c=input("Ciudad: ")
address(s,pc,c)
##############################################################
def restar(a,b):
    print(a-b)
restar(5,2)
restar(2,5)
restar(b=2,a=5)
restar(5,b=2)
#restar(a=5,2) esto da error por posicionamiento
#########################################################
def multi(a,b):
    return a*b;
print(multi(3,5));
###############################################################
def wishes():
    print("My wishes")
    return "Happy birthday";
wishes()
x=wishes();
print(x)
#################################################################
def hiall(lista):
    for name in lista:
        print("Hola",name);
hiall(["Vel","Leo"])
##############################################
def crealista(n):
    lista1=[];
    for i in range(n):
        lista1.append(i)
    return lista1
print(crealista(4))
