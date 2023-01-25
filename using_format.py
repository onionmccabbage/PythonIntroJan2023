# there are many ways to format printed output

def main():
    gen = (i**3 for i in range(1,11)) # a generator all the cube nubmers 1-10
    for n in gen:
        print(n, end=', ') # each print will finish with a COMMA not a new line
    # we can use formal 'format' statements
    x = 1.2345
    y = 98.765
    print( 'The value of x is {} and y is {}'.format(x, y) ) 
    print( 'The value of x is {0:.2f} and y is {1:.2f}'.format(x, y) ) 
    print( f'The value of x is {x:.2f} and y is {y:.2f}' ) 

if __name__ == '__main__':
    main()