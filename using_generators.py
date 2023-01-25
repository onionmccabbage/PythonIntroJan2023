# Python has a 'generator' which is very efficient
# for example, we may need a bunch of square numbers

# we can write a list
sq_l = [1, 2, 9, 16, 25, 36] # all these values must persist in memory
# or we can generate the values (they never persist in memory)
sq_g = ( num*num for num in range(1, 11) ) # we now have a generator object
print( type(sq_g) )
# here is the way to access members of our generator
print( sq_g.__next__() ) # this will yield the NEXT value in the generator
print( sq_g.__next__() ) # 4
print( sq_g.__next__() ) # 9

if 31 in sq_g: # easy way to check a value
    print('yes')
else:
    print('no')

# we can iterate over the values from a generator
for value in sq_g: # this will yield EVERY remaining value from our generator
    print(value) # 16, 25, 36, etc.