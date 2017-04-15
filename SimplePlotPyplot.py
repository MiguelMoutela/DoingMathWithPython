'''
Simple plot using pyplot
'''

import matplotlib.pyplot

def create_graph(x_numbers, y_numbers):

    matplotlib.pyplot.plot(x_numbers, y_numbers)
    matplotlib.pyplot.show()

if __name__ == '__main__':
    xcount = 0
    x_numbers = []
    ycount = 0
    y_numbers = []
    while True:
        x_numbers.append = input('Enter an x value: ')
        answer = input('Would you like to input another x value? (n) for no ')
        xcount = xcount + 1
        if answer == 'n':
            break
    print('You have {} x values.'.format(xcount))
    while True:
        y_numbers.append = input('Enter a y value: ')
        answer = input('Would you like to input another y value? (n) for no ')
        ycount = ycount + 1
        if answer == 'n':
            break
    print('You have {} y values.'.format(ycount))

    create_graph(x_numbers, y_numbers)
        
        
            
            
        
        
    
