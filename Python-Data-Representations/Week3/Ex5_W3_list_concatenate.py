"""
Concatenate one list onto another
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

new_list = example_list + [0,0,0]

print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]