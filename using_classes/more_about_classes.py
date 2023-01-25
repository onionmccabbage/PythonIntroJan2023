# we can write methods that belong to the class itself

class Duck(): # this class implicityl injerists from object
    count = 0 # this property belongs to the CLASS
    def __init__(self,n):
        self.name = n
        Duck.count += 1 # we can increment the total count of duck instances
    def __str__(self):
        return f'{self.name}'
    @classmethod # we want a method that can be called on the CLASS (rahter than on instances)
    def numDucks(cls): # this does NOT take 'self'
        return cls.count
    @staticmethod # no self, no class, this is a static method
    def promo():
        return 'These ducks are brought to you by Duck and Go'

if __name__ == '__main__':
    donald = Duck('Donald')
    howard = Duck('Howard')
    ella   = Duck('Ella')
    zero   = Duck('Zero')
    print(Duck.numDucks()) # 4
    print(Duck.promo())
    print(ella.promo())
    print(ella.numDucks())
