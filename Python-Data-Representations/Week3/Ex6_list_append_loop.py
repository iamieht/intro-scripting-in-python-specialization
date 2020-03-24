"""
Append several item to a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

for num in [0,0,0]:
    example_list.append(num)
    
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]