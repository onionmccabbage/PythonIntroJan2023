'''
It is a good idea to write a docstring - a documentation string
This is done using THRE quotes like this
'''

# checking type instances
q = 1.23

if isinstance(q, int):
    print(f'{q} is an integer')
elif isinstance(q, float):
    print(f'{q} is a floating point value')

# we can also cast something to a type
r = range(0,10) # here we have a range data type
t = tuple(r) # now we have a tuple
print(t, type(t))
