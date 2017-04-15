# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:06:04 2017

@author: tater
"""
from scipy import *
from matplotlib import pyplot as plt

def f(x):
    return 2*x+1
z = []
for x in range(10):
    if f(x) > pi:
        z.append(x)
    else:
        z.append(-1)
print(z)