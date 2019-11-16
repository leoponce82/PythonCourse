# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:11:01 2019

@author: CEC
"""

def isYearLeap(year):
    if type(year)==int:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return True;
                return False;
                
            return True
        
        return False;
    else:
        return None
#

def daysInMonth(year, month):
    if  month>0 and month<13:
        mesesLeap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        meses={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if isYearLeap(year)==True:
            return mesesLeap[month]
        return meses[month]
    else: 
        return None;

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
