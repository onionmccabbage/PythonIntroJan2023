# every piece of code is in a scope
# any code that is not in a block is in the global scope
# by the way - we tend to avoid using the global scope
# here are some values in the global scope
g = 'this is a global variable'
n = 42

# here is a block of code (every code block has its own scope)
def fn():
    global g # now 'g' will refer the global variable
    g = 'this is scoped to the function'
    print(g)
    return g

if __name__ == '__main__':
    print(g) #this prints the original global value
    fn()
    print(g) # its value has been replaced inside the function