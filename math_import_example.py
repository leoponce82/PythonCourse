# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:23:54 2019

@author: CEC
"""

#################
"""
Formas de importar un modulo
import <module> #para llaamr entidades llamar como math.<entidad>
import <module> as <alias>
from <module> import <entidad>
from <module> import * #no se ocnoce las entidades a importar pero no afrece facilidad de exploracion
from <module> import <entidad> as <alias_de_entidad>
"""
####################
import math
ad=90
ar=math.radians(ad)
ad=math.degrees(ar)

print(ad==90.)
print(ar==math.pi/2.)
print(math.sin(ar)/math.cos(ar)==math.tan(ar))
print(math.asin(math.sin(ar))==ar)

import datetime
time=datetime.datetime.now()
print(time.isoformat())

from platform import machine
print(machine())
