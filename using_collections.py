from random import randint

# we can easily populate collections
odds = range(1,100,2) # all the odd numbers from 1 to 100
print(odds, type(odds)) # we have a 'range' data type
for item in odds:
    print(item)

# we can make a random number then say if it is odd or even
r = randint(0,100)
if r in odds: # check to see if a value exists in a collection
    s = 'odd'
else:
    s = 'even'
print( f'the random numbmer {r} is {s}' )