# file input and file output (fifo)
# we smetimes need more control over the way we write or read text files
t = 'here is a large amount of text to be written to a log file'

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

# read text back again, possibly a bit at a time
# the 'with' operator is useful here
with open('mylog.txt', 'rt') as fin: # read text
    # retrieved = fin.readline() # .readine would read just one line
    retrieved = fin.readlines()[0:5] # .realines would read all or a specific num of lines
    # retrieved = fin.read(24) # read the specified size
    print(retrieved)
    # no need to close - when 'with' is done, the fin object is closed automatically






