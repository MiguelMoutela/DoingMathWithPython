'''
Compare City Temps
'''
from matplotlib import pyplot as plt

def create_graph(x_num, y_num1, y_num2):
    plt.plot(x_num, y_num1, x_num, y_num2)
    plt.legend(['London', 'Glasgow'])
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature (C)')
    plt.title('Temperature in London and Glasgow on 3/26/17')
    plt.show()

if __name__ == '__main__':

    hour = [7, 10, 13, 16, 19, 22]
    LondonTemps = [7, 10, 13, 14, 11, 9]
    GlasgowTemps = [3, 7, 13, 15, 13, 9]

    create_graph(hour, LondonTemps, GlasgowTemps)
    
    


    
