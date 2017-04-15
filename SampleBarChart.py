# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:49:26 2017

@author: tater
"""

from scipy import *
from matplotlib import pyplot as plt

def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.ticks(positions, labels)
    plt.xlabel('Steps')
    plt.ylabel('Day')
    plt.title('Number of steps walked')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    steps = [6534, 7000, 8900, 10786, 3567, 11045, 5095]
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    create_bar_chart(steps, labels)