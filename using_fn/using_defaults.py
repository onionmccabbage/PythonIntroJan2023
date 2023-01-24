# When using functions it is possible to specify default values for arguments

def triangle(x=3, y=4): # we can provide defaults in case values are not available
    '''
    This function will return the hypotenuse of a right-angled triangle
    given x and y, h = (x*x + y*y)**0.5
    '''
    h = h = (x*x + y*y)**0.5
    return h

# we only run the following code if this module is run DIRECTLY (not if this module gets imported)
if __name__ == '__main__':
    hypot = triangle(3, 4) # we override the function default values with our own values
    print(hypot) # 5.0
    def_hypot = triangle() # no arguments provided so the function will use its default values
    print(def_hypot) # 5.0
    