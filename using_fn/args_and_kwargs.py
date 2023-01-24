# we can combine args and kwargs...

def fn(*args, **kwargs):
    print(args) # show the positional arguments tuple
    print(kwargs) # show the keyword arguments dict

if __name__ == '__main__':
    fn()              # call with no args and no kwargs
    fn(3, 4, 5)       # call with args and no kwargs
    fn(x=4, y=4, z=5) # call with no args but with kwargs
    fn(3, 4, z=5)     # call with args and also kwargs
