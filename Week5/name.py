import sys

# check for errors 
if len(sys.argv) < 2: # if too few 
    sys.exit("Too few argumnets")

# elif len(sys.argv) > 2: # if too many 
#     sys.exit("Too many arguments")
# print name tags

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)



