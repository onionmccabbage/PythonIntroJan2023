print('anything NOT inside the "if" will be run on import')

def writeBytes(data):
    '''write some bytes to a file'''
    try:
        fout = open('bfile', 'wb') # 'wb' means (over)write bytes (rather than t for text)
        fout.write(data)
        fout.close() # tidy up
    except Exception as err:
        print( f'here was an eror {err}' )

def readBytes():
    '''read back bytes from a byte file'''
    try:
        fin = open('bfile', 'rb') # 'rb' means read bytes
        r = fin.read()
        fin.close()
        print(r)
    except Exception as err:
        print( f'here was an eror {err}' )       

# we need to avoid running the module if its imported
if __name__ == '__main__':
    # file input and file output using Bytes
    b = bytes( range(0, 255) ) # the first 255 characters as bytes
    # a byte is eight bits
    print(b) # the b'' at the start of the string tells us it is a Byte string
    # we can invoke our functions here
    writeBytes(b) # pass our byte string into our function
    print('this line runs solely because this module was run directly')