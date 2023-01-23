'''
Python has no practical limits on the size of data values
you are only limite dby the resources of your machine
'''

import sys # sys represents the system on which Python is running

# here is a big number
big = 10**10000 # careful!!!

print(big)

# we cna get an idea of tis system capabilities
print(sys.maxsize)
print(sys.float_info)

# Epsilon represents the smallest accuracy this system can manage
# remember ALL computers are digital not real
