# explore 'if' logic

s = 'words'

# double-equals checks equality
if type(s) == str: # indentation matters in Python
    print('it is a string')

n = 3
# the colon : indicates the start of a block of code
if n <=10: # > < etc.
    print('it is less than ten')
    # all related code after a colon MUST be indented
print('this runs anyway - it is not indented so it is NOT part of the above code block')

b = False
if b != True: # ! means NOT
    print('it is not true')

# ask the user
i = input('please enter something: ') # in Python 2 we use raw_input()
# CAUTION - input ALWAYS returns a STRING
print(type(i))
# act upon what they typed
if i == 'go':
    print('you entered go')
elif i == 'stop': # elif means else if
    print('stopping')
elif i == 'wibble':
    print('!')
elif i.isnumeric(): # check if the value is a positive integer (no decimals)
    n = int(float(i)) # it is safest to use int(float(i))
    # NB these curly brackets are NOTHING to do with 'set'
    print(f'you entered the integer {n} the original string was \'{i}\'   ') # tidy syntax to inject values into a formatted string
    # we can further check....
    if n > 10:
        print('bigger than ten')
    else:
        print('ten or less')
else: # we can inject any values into a string using {}
    print('something other was entered {}'.format(i))