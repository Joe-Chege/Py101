# Strings >> A collection of characters is termed as a string
#It is a collection of characters closed within single, double or triple quotation marks.

# Here is a good example of stings 

print('Am loving every bit coding in python') # single quatation

doubles = "In double quotes there is still sn output..." # double quotation
print(doubles)

print("$") # single character

nill = ""  # prints an empty space hence note that python is sentitive with even space 
print(nill) # prints an empty line

Triple = """This is tiple quatation string"""
print(Triple) # amaizingly it printed

## The length of a strings can be defined using len()built-in function.

# Here is an example of knowing a length

print(len(Triple)) # the lenth of triple string is 30

## Indexing 

"""
In a string, every character is given a numerical index based on its position.
A string in Python is indexed from 0 to n-1 where n is its length.
This means that the index of the first character in a string is 0.
"""

## Accessing Characters 
"""
Each character in a string can be accessed using its index. 
The index must be closed within square brackets, [], and appended to the string.
"""
# Here is an example of accesing characters with the help of indexing
example = 'accessing characters'
fifth= example [4] # accessing the first character
print(fifth)
