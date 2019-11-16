# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:55:47 2019

@author: CEC
"""

def badFun(n):
    try:
        return n/0
    except ArithmeticError:
        print("I did it again!")
        raise
try:
    badFun(0)
except ArithmeticError:
    print("I see!!!!")
    
print("THE END")