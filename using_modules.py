# we can import functions we have already written to use in another module
# import will look in
# the current drectory
# any Python path 
# you can specify an absolute or relative path
# in this case we access a module that is inside a package (i.e. folder)
from my_util.fifo_bytes import writeBytes

# ask the user
i = input('what needs to be written? ')
# the encoding is what kind of text we have - UTF8 is western text
b = bytes(i, encoding='UTF8') # convert it to bytes
# write to bytes
writeBytes(b)