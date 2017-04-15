'''
Exploring a Quadratic Function Visually
'''
from matplotlib import pyplot as plt

def create_graph(x,y):
    plt.plot(x, y)
    plt.xlabel('x-value')
    plt.ylabel('y-value')
    plt.title('y = x^2 + 2x + 1')
    plt.show()

if __name__ == '__main__':

    print('A graph will be generated of your function.')
    x_vals = list(range(-10,10,1))
    y_vals = []
    for x in x_vals:
        #Calculate the value of the quadratic function y = x^2 + 2x + 1
        y_vals.append(x**2 + 2*x + 1)

    create_graph(x_vals, y_vals)

    
    
