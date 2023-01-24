# file input and file output (fifo)
# we sometimes need more control over the way we write or read text files
t = 'here is a large amount of text to be written to a log file take two'

# if we want we can pass in arguments to the function
def fileOutput(t): # here we define a function
    # this is a good example where we should use exception handling
    try: # Python will try to execute this block
        fout = open('mylog.txt', 'at') # append text
        size = len(t) # how many characters in our text string
        offset = 0
        chunk = 24 # here we choose how many characters to write in one go
        # next we will write our text string out, 24 characters at a time
        while True:
            if offset > size:
                fout.write('\n') # all the text has vbeen written, so terminate with a new line character
                break # we're all done!
            else:
                # [start : stop-before]
                fout.write( t[offset:offset+chunk] ) # we wtie only 24 characters at a time
                offset += chunk # += means ad the value to the current value
        fout.close() # tidy up
    except FileExistsError as err:
        print('sorry you cannot write to the file if it exists already')
    except Exception as err: # if something goes wrong ten Python will jump to this block
        print( f'There was a problem: {err}' )
    # you can have maultiple except blocks each for different exceptions
    finally: # this block always runs, whether there is an exception or not
        pass # here we choose to do nothing


def fileInput(): # here is another function
    # read text back again, possibly a bit at a time
    # the 'with' operator is useful here
    with open('mylog.txt', 'rt') as fin: # read text
        # retrieved = fin.readline() # .readine would read just one line
        retrieved = fin.readlines()[0:5] # .realines would read all or a specific num of lines
        # retrieved = fin.read(24) # read the specified size
        print(retrieved)
        # no need to close - when 'with' is done, the fin object is closed automatically

# nothing happens until we CALL the function
while True:
    t = input('what needs to be writen to the log? ')
    if t.lower() == 'q': # s we don't need to check both cases
        break
    if t.lower() == 'r':
        # NB we can only call functions AFTER they have been declared
        fileInput() # invoke our file reader function
    else:
        fileOutput(t) # here we pass in the value of t we wish to use
