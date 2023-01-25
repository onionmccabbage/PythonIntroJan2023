# we can write simple test to make sure our code behaves as expected
import doctest # this will let us write tests
def cube(x):
    '''we can write doctest in the documentation string
    >>> cube(3)
    27
    >>> cube(4)
    64
    '''
    return x*x*x

if __name__ == '__main__':
    doctest.testmod(verbose=True) # we invoke our tests
    print( cube(3) ) # 27