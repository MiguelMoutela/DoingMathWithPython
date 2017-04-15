# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:29:02 2017

@author: tater
"""

from scipy import *
from matplotlib import pyplot as plt

def create_bar(data, labels):
    num_bars = len(labels)
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel("Dollars")
    plt.ylabel("Categories")
    plt.title('Expenditures per Category')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    num_cat = int(input('Enter the number of categories: '))
    category = []
    expenditure = []
    for i in range(0, num_cat):
        category.append(str(input('Enter category: ')))
        expenditure.append(int(input('Expenditure: ')))
        
    create_bar(expenditure, category)
    