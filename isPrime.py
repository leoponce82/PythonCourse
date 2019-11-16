# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:26:15 2019

@author: CEC
"""

def isPrime(j):
    if j==0:
        return False;
    if j==1:
        return False;
    if j==2:
        return True;
    for i in range(2,j):
            if j%i==0:
                return False;
    return True;

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

        