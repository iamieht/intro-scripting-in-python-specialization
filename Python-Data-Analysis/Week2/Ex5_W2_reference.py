"""
Solution - Analyze a reference issue involving a nested list
"""

# Create a nested list
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    # nested_list.append(zero_list)
    nested_list.append(list(zero_list))    # Corrected code
print(nested_list)
    
# Update an entry to be non-zero
nested_list[2][1] = 7
print(nested_list)


# Erroneous output
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

# Desired output
# [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
# [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]


# Explanation

# Line 13 is unintentionally updating all 5 entries in nested_list due to a referencing issue.

# Line 9 is creating five references to the SAME onject (the list zero_list) in nested_list.
# Thus, updating one reference to zero_list in nested_list in line 13 updates 
# the other four references to zero_list in nested_list simultaneously. 

# To visualize this reference issue in Python Tutor, visit the URL https://goo.gl/hT4MM3.
# Note the entries in nested_list all refer to SAME list.  

# The solution to this problem is to make a NEW copy of zero_list each  time append()
# is executed. To do this, simply replace zero_list by list(zero_list) in line 9

# To visualize corrected code in Python Tutor, visit the URL https://goo.gl/4nifEg.
# Note that each entry in nested_list now refers to a DISTINCT list.  As a result,
# updates to one item in nested_list do not affect any other part of nested_list.

