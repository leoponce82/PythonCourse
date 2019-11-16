# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:44:36 2019

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
        print("Año no valido")
        return None
#

def daysInMonth(year, month):
    if  month>0 and month<13:
        mesesLeap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        meses={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if isYearLeap(year)==None:
            return None;
        if isYearLeap(year)==True:
            return mesesLeap[month]
        return meses[month]
    else: 
        print("Mes no valido")
        return None;


    
    
def dayOfYear(year, month, day):
    dias=0
    if  day>0 and day<32:
        if daysInMonth(year,month)==None:
            return None
        for i in range(1,13):
            dias=dias + daysInMonth(year,i)
        return dias;
    else:
        print("Dia no valido")
        return None;

    
    

print(dayOfYear(2004, 12, 31))
