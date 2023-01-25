# use the built in structures whenever they suit your purpose
p = {'fname':'Timnit', 'lname':'Gebru', 'age':42} # here we encapsulate a person

p['age'] = True # oh dear

# the built in structures give no mchanism to validate their values
# we can write a class to ensure we validate the data members

class Person: # by convention we usse initial cap for a class name
    '''This class encapsulates a Person with positive integer age'''
    def __init__(self, a, n): # every function in a class MUST take 'self' which represents the class
        self.age  = a # even though .age does not look like a function, Python will call the setter function property
        self.name = n
    # we then write methods to set or get the properties of this class
    @property # this use of @ here is called 'decorator syntax'
    def age(self): # this is implicitly the 'getter' for the age property
        return self.__age # the double underscores make the __age property 'mangled'
    @age.setter
    def age(self, a): # this is the 'setter' for the age property
        # we can now validate the data
        if type(a)== int and a>0:
            self.__age = a # we set the 'mangled' property value
        else:
            self.__age = 42 # we can set a sensible default
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n): # we can validate the name as a non-empty string or set a default
        if type(n)==str and n != '':
            self.__name = n
        else:
            self.__name = 'default'
    # old-skool Python can use the following syntax
    #     name = property(getname, setname)
    #     age  = property(getage, setage)

if __name__ == '__main__':
    # here we can make use of our class
    a = Person(32, 'Ada')
    b = Person(False, '') # this will use the class defaults
    # NB we CANNOT directly access __age or __name
    print( a.age, a.name ) # we can access class properties using dot syntax
    print( b.age, b.name ) # we can access class properties using dot syntax



