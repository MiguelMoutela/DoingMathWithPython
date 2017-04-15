# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:38:12 2017

@author: tater
"""

from scipy import *
from matplotlib import pyplot as plt

'''
Calculating the median
'''

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()
    
    # Find the median
    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to int and match the numbers to their list positions
        # since lists start at position 0
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # convert to int and patch positions
        m = int(m) - 1
        median = numbers[m]
    return median

if __name__ == '__main__':
    donations = [100, 50, 60, 40, 70, 500, 500, 70, 1000]
    
    median = calculate_median(donations)
    N = len(donations)
    print('Median donation over {0} days is {1}'.format(N, median))
    
        
