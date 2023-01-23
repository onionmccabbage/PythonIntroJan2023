# the dictionary data type is a mutable non-indexed collection of any data type

# careful - curly brackets can mean a set OR a dictionary. It depends on the syntax
# here we have a collection of key:value pairs
# the Python code style recommends all the keys should be strings
# BUT keys can be of ANY data type
d = {'id':'Timnit', 'age':42, 'member':True, 'codes':[4,3,2], 3:55}

print(f'The id is {d["id"]} age {d["age"]} membership is {d["member"]}')

# we can add members to a dictionary
d['languages'] = ('python', 'Java', 'C') # here we have a tuple
# we can mutate members of a dictionary
d['codes'] = False # no problem using a different data type

# we can iterate over the members of a dictionary
# (k, v) is a TUPLE of the key and value from the dict
for (k, v) in d.items(): # items() is ALWAYS the members of a dictionary
    print(f'The key is {k} and the value is {v}')

# other ways to create collections
w = list() # an empty list
x = tuple() # an empty tuple
y = dict() # an empty dictionary

m = [] # an empty list
n = () # ...
p = {} # is this a set or a dict ...?

# be careful creating a one-member tuple
e = (3) # this is NOT a tuple, it is just an integer
print(type(e))
f = (3,) # this is now a one-member tuple
print(type(f))





