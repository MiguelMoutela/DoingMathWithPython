'''
Even Odd Vending Machine
'''

def even_odd(a):
    if a % 2 == 0:
       print('{0} is an even number'.format(a))
       mylist = list(range(a, a+19, 2))
       print(mylist)
       
    else:
        print('{0} is an odd number'.format(a))
        mylist = list(range(a, a+19, 2))
        print(mylist)

if __name__ == '__main__':
    a = input('Please enter an integer: ')
    even_odd(int(a))
    
