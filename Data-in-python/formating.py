## String Formatting

"""
String formatting means substituting values into a string. Following are some use cases of string formatting:
Inserting strings within a string
Inserting integers within a string
Inserting floats within a string
"""
# here is an example for inserting string within a string

string1 = "I like %s" % "coding "
print(string1) # 'I like coding'

temp = "swimming"
string2 = "I love %s" % temp
print(string2) # 'I like swimming'

string3 = "I like %s and %s" % ("coding", temp)
print(string3)  # 'I like coding and swimming'

# Here is an example for inserting integers within a string


my_string = "%i + %i = %i" % (7,5,12)
print(my_string) # '7 + 5 = 12'
## The %i is the format specifier, which tells Python to insert the integers 

# Here is an example of inserting floating within a string

string1 = "%f" % (1.11)
print(string1) # '1.110000'

string2 = "%.2f" % (1.11)
print(string2) # '1.11'

string3 = "%.2f" % (1.117)
print(string3) # '1.12'

""" 
%f is used to substitute floats within a string. Note, string1 includes extra zeroes. How about limiting 
1.11 to two decimal places, We can use %.2f
"""

