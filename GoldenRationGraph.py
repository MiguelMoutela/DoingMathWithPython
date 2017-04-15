# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:05:43 2017

@author: tater
"""

from scipy import *
from matplotlib import pyplot as plt
from pylab import axis

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    # n > 2
    a = 1
    b = 1
    # first two numbers in the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    
    return series

def create_graph(y_val):
    plt.plot(y_val)
    plt.xlabel("Numbers")
    plt.ylabel("Ratio")
    plt.title("The Golden Ratio")
    plt.show()

if __name__ == '__main__':
    
    # call the fib function and store it in a list
    series = fib(20)
    print(series)
    
    length = len(series)
    # print(length)
    
    ratios = [1]
    for i in range(0,21):
        j = i+1
        x = series[i]
        #print(x)
        y = series[j]
        #print(y)
        result = y/x
        format(result, '1.4f')
        #print(result)
        ratios.append(result)
    
    #print(ratios)
 
    #print(series)
    
    create_graph(ratios)
    


        
