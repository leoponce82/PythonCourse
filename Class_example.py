# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 08:24:36 2019

@author: CEC
"""

class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name: ", self.name,"Salary: ",self.salary)
            
emp1=Employee("Zara",2000)
emp2=Employee("P&B",5000)

emp1.displayEmployee()
print()
            