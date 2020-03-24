"""
Shuffle the items in a list
"""
import random

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

random.shuffle(example_list)
   
print(example_list)


# Output - note that order of second list may vary due to randomness
#[2, 3, 5, 7, 11, 13]
#[11, 2, 7, 5, 13, 3]