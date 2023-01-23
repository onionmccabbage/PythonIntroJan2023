# many ways we can access external data
# we can read and write from...
# a text file (such as a log file)
# we begin by writing text to a file
s = 'here is some log info: error message oops'
# first we need to open the file. 'wt' means (over)write text
# 'at' will append text
# 'xt' will only write if the file does not already exist
fout = open('mylog.txt', 'at') # fout is a file access object (NOT the file itself)
print(s, file=fout)
fout.close() # we no longer want to write to the file

# we can read back from the file
fin = open('mylog.txt', 'rt') # 'rt' will read text
retrieved = fin.read()
print(retrieved)
fin.close() # always a good idea to tidy up

# a byte file
# an API url

# on the next course (advanced python) we see
# read/write database
        
# on the third course (further advancecd python) we read/write between micro-services