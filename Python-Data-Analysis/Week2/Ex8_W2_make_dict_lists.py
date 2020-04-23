"""
Write a function make_dict_lists(length) that returns a dictionary whose keys are in range(length) and whose
corresponding values are lists of zeros with length matching the key
"""


# Add code here
def make_dict_lists(length):
    """
    Given an integer length, return a dictionary whose keys
    lie in range(length) and whose corresponding values are 
    lists of zeros with length matching the key
    """
    result_dict = dict()

    for idx in range(length):
        result_dict[idx] = [0] * idx
    
    return result_dict



# Tests
print(make_dict_lists(0))
print(make_dict_lists(1))
print(make_dict_lists(5))


# Output
#{}
#{0: []}
#{3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}
