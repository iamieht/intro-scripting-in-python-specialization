"""
Count the number of times that a word appears in string of text
"""

def word_count(text, word):
    """
    Given a string text consist of words separate by spaces and a string word
    (with no spaces), return the number of times that word appears in the text
    """
    
    words = text.split()
    return words.count(word)


# Tests

print(word_count("this pigdog is a fine pigdog", "pigdog"))
print(word_count("this pigdog is not a dog", "dog"))
print(word_count("this pigdog is not a pig", "pigdog"))

# Output
#2
#1
#1