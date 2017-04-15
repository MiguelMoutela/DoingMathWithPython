'''
Multiplication Table Printer
'''

def multi_table(a, b):

    for i in range(1,b+1):
        print('{0} x {1} = {2}'.format(a, i, a*i))
        

if __name__ == '__main__':
    while True:
        a = input('Enter a number: ')
        b = input('How many multiples would you like to see?: ')
        multi_table(int(a), int(b))
        answer = input('Would you like to exit? (y) for yes ')
        if answer == 'y':
            break
    
    
