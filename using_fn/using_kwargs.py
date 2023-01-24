# Sometimes we need to call a function with one, two or three or more arguments
# we may not know exactly how many arguments

# we use **kwargs

def wibble(**kwargs): # **kwargs allows us to pass in zero or more KEYWORD arguments
    ## all the KEYWORD arguments now exist in a dictionary called kwargs
    print(kwargs) # see how many potitional argumetns were passed in
    if 'category' in kwargs.keys() : # we have a 'category' arguments
        url = f"https://jsonplaceholder.typicode.com/users/{ kwargs['category'] }"
    if 'id' in kwargs.keys(): # we have an id argument
        url = f"https://jsonplaceholder.typicode.com/users/{kwargs['category']}/{kwargs['id']}"
    return url # we can only return ONCE from a function

if __name__ == '__main__':
    url = wibble(category='posts') # call with one keyword argument
    print(url)
    url = wibble(category='posts', id=1) # call with two keyword arguments ...
    print(url)
