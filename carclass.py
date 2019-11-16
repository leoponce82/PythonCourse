# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:28:24 2019

@author: CEC
"""

class Car():
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
    def drive(self):
        """Simulate driving."""
        print("The car is moving.")
my_car = Car('audi', 'a4', 2016)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.drive()

my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)
my_new_car = Car('audi', 'a4', 2016)
my_new_car.fuel_level = 5 
# Metodo Incrementar un atributo
def update_fuel_level(self, new_level):
    """Update the fuel level."""
    if new_level <= self.fuel_capacity:
        self.fuel_level = new_level
    else:
        print("The tank can't hold that much!")
