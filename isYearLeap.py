# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:45:34 2019

@author: CEC
"""
def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True;
            return False;
            
        return True
    
    return False;
#
# Su codigo AQUI
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
        

