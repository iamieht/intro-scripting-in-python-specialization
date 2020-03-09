"""
Another example of slice selection for lists
"""

# Create a string formed by selecting the first three characters of example_string
# plus the last three characters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[:3] + example_string[-3:]
print(solution_string)

# Output should be 
#It's just a flesh wound
#It'und