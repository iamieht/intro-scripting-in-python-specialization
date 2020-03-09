"""
Function that uses format to create a nametag
"""


def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name 
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    
    # enter code here
    return "Hi! My name is {}. This lecture covers {}.".format(first_name, topic)

    
# Tests

print(make_nametag("Scott", "Python"))
print(make_nametag("Joe", "games"))
print(make_nametag("John", "programming tips"))


# Output

#Hi! My name is Scott. This lecture covers Python.
#Hi! My name is Joe. This lecture covers games.
#Hi! My name is John. This lecture covers programming tips.