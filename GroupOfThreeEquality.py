def any_equal(a, b, c):
    if a != b and a != c and b != c:
        print('No inputs match')
    elif a == b and b !=c:
        print('At least two inputs are the same')
    elif b == c and c != a:
        print('At least two inputs are the same')
    else:
        print('All inputs match.')

if __name__ == '__main__':
    a = input('Enter your first value: ')
    b = input('Enter your second value: ')
    c = input('Enter your third value: ')

    any_equal(a, b, c)
              
        
