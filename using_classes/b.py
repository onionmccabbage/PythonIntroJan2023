# here we will extend our 'Person'
# we can also have mangled functions (and normal function)

from a import Person

class Coder(Person): # this class will inherit everything from the Person class
    '''In addition to name and age, a Coder will have a 'language' peroperty'''
    def __init__(self, a, n, l):
        super().__init__(a, n) # call the init method of the parent class
        self.language = l  # unless we make this a property, this will not be validated
    # make language into a validated property
    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, l):
        self.__language = self.__validate(l)
    # we can write normal functions in a class (they are known as 'methods')
    def __str__(self): # we can override the built-in '__str__' method to make our own print response
        # CAREFUL - we use 'self' to refer to the current isntance
        return f'Name:{self.name} Age:{self.age} Language:{self.language}'
    # we can also mangle methods, so they are only available within the class
    def __validate(self, value):
        if type(value)==str and value !='':
            return value
        else:
            return 'default'

if __name__ == '__main__':
    # when we create an instance of a class, it WILL call __init__
    grace = Coder(98, 'Grace Hopper', 'Assembly')
    # the 'print' statement in Python will ALWAYS looks for a __str__ method on the object being printed

    # print( grace.prettyPrint() ) # the brackets indicate we are calling a function
    print(grace) # this will call our __str__ method
        