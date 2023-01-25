# we already saw the __str__ being overriden
# we can override MANY features in Python

# here is a class which has its OWN definition for 'equality'
class Word():
    '''This class overrides the equality operator'''
    def __init__(self, text):
        self.text = text # here we are not using get/set methods
    # this next function declares our OWN meaning for the equality operator
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    word1 = 'Hello'
    word2 = 'hello'
    print( word1==word2 ) # False
    w1 = Word('Hello')
    w2 = Word('hello')
    print( w1 == w2 )  # True
    # print( w1 == word2 ) # fails - they must be of the same data type
    print( w1.__doc__  ) # this will print the docstring