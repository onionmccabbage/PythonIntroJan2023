
# a 'for' loop
for i in range(-5, 5, 3): # range gives us an iterable from 'start' to 'stop-before' (step)
    print( f'The iterator is {i}' )

# a 'while' loop
from random import randint # the random library is always available for import
x = 0
while x !=5: # while is often used to repeatedly check a value until it matches
    x = randint(0,6) # random integer from 0 to 6 inclusive
    print(f'The random integer is {x}')