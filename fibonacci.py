# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:18:43 2019

@author: CEC
"""
def fibonacci(limit):
    #limit=int(input("Ingrese numero de iteraciones: "))
    a=0;
    b=1;
    print("Resultado= ")
    R=[];
    for i in range(limit):
        res=a+b;
        a=b
        b=res
        print(res,"\n")
        R.append(res)
    print(R)
        

    
    
    

