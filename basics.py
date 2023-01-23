# here is a comment
a = 3 # an integer (implicitly)
b = 7.2 # float 4.888 
c = a/b

print(c, type(c), type(a)) # Add an integer to a float gives a FLOAT

# other operators
print(b//a) # integer division
print(b%a)  # show remainder

print(b**3) # raise to a power

# in Python data types are not fixed, they are dynamic
a = 'hello' # a string type
print(type(a))

# we can try to cast a data type
c = int(b) # we cast the float data to an int data
print(c, type(c)) # prints the class (i.e. the data type) of the variable

# a few more primitive data types
d = True # or False (boolean data type)
e = None # useful!!

# the string collection type - a string is an indexed collection of characters
c = 'nearly coffee'
# Square brackets - return [start : stop-before : step]
print(c[0:12:2]) # prints member 0 to 4 of the indexed collection
print(c[::-1]) # it uses default start and stop values
c = ''.join(reversed(c)) # another way!!

# the 'string' data type is immutable
my_words = 'here is a rather long string of text'
# my_words[0] = 'H' # NO!!! the string canot be changed - it is immutable

# other collection data types: list, tuple, set and dictionary
l = [3, 2, 1] # we have a list - an indexed, mutable collection
l[1] = my_words # a list can contain ANY mixed data types
# we can mutate a list
l.append(a)
l.pop() # removes the top-most index member
print(l, type(l), l[1], len(l))

# tuple is an indexed immutable collection of any data types
t = (7, 6, 5, a, b, c)
print(t, type(t), len(t))
# t[0] = 'nope cant change it' # no cannot do this - immutable tuple

# the set data-type (mutable)
s = {7,6,5,4,3,7} # the members of a set are unique (of any data type)
s.add('7')
s.add(7.0)
s.remove(4)
print(s, type(s))

# conclusion: [] for list, () for tuple, {} for set, quotes for string