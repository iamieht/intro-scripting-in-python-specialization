"""
Analyze an example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Another reference to list1
list2 = list1

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment

#Both lists point to the same memory address, as they are the same referenced object


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]