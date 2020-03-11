"""
Take a list of integers and concatenate their digits
"""

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    concatenated_number = ''

    for num in int_list:
        concatenated_number += str(num)
    
    return int(concatenated_number)

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000