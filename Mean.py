# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:01:00 2017

@author: tater
"""

from scipy import *
from matplotlib import pyplot as plt

'''
Calculate the mean
'''

def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total/count
    
    return mean

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean donation over the last {0} days is {1}'.format(N, mean))
    