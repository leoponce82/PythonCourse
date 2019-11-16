# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:31:17 2019

@author: CEC
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()