"""
Analyze another example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment
#list2 is a new list independant from list1, so mutating one list do not mutate the other one  



# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]