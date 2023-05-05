## Sting Slicing
# Slicing is the process of obtaining a portion (substring) of a string by using its indices
# basically geting a part of a sting using the knowledge we on indexing use this code string[start:end] 
"""
string[start:end] >> start is the index from where we want the substring to start.
 >>>>end is the index where we want our substring to end
"""
# Here is an example of slicing

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end

## Slice with a step 
# It uses this code string[start:end:step] where step is where the next output is determind by the number of jumps

# Here is an example 

string = "one of this days i will so good in this that nations will look for me"
print(string[1:7:2]) # A step of 2
print(string[0:10:4]) # A step of 4

"""
Reverse Slicing 
Strings can also be sliced to return a reversed substring. 
In this case, we would need to switch the order of the start and end indices.
"""
# Here is an example 

string = "one of this days i will so good in this that nations will look for me"
print(string[10:3:-1]) # A step of 1 in the opposite
print(string[7:5:-2]) # A step of 2

"""
Partial Slicing 
One thing to note is that specifying the start and end indices is optional.
If start is not provided, the substring will have all the characters until the end index.
If end is not provided, the substring will begin from the start index and go all the way to the end.
"""

#n# here ia an example 

string = "one of this days i will so good in this that nations will look for me"
print(string[:5]) #
print(string[4:])
print(string[:])
