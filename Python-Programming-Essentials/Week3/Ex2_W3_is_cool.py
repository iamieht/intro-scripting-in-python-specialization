"""
Compute whether a person is cool.
"""

###################################################
# Is cool formula
# Student should enter function on the next lines.
def is_cool(name):
    '''
    Returns True if name is "Joe", "John" or "Stephen" 
    '''
    return name == "Joe" or name == "John" or name == "Stephen"


###################################################
# Tests
# Student should not change this code.

name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
