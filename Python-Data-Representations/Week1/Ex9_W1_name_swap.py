"""
Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    separated_names = name_string.split()
    return separated_names[1].capitalize() + ' ' + separated_names[0].capitalize()
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John