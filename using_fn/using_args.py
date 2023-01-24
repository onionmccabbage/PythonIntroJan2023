# Sometimes we need to call a function with one, two or three arguments
# we may not know exactly how many arguments

# we use *args

# CAREFUL! the order of positional arguments is VITAL
def wibble(*args): # *args allows us to pass in zero or more positional arguments
    ## all the positional arguments now exist in a tuple called args
    print(len(args)) # see how many potitional argumetns were passed in
    if len(args) == 0: # we have no arguments
        return "https://jsonplaceholder.typicode.com/users"
    elif len(args) == 1:
        return f"https://jsonplaceholder.typicode.com/users/{args[0]}"
    elif len(args) == 2:
        return f"https://jsonplaceholder.typicode.com/users/{args[0]}/{args[1]}"

if __name__ == '__main__':
    url = wibble() # call with no arguments
    print(url)
    url = wibble('posts') # call with one argument
    print(url)
    url = wibble('posts', 1) # call with two arguments ...
    print(url)
