"""Logical Operators
They are 3 in number - and 
                     - or
                     -not
In the following code i will be showing how to use it while looping in python"""

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))

if (a>b) and (a>c):
    print("A is greater")


elif (b>a) and (b>c):
    print("B is greater")

elif (c>b) and (c>a):
    print("C is greater")

elif (a==b) and (a>c):
    print("a=b greater than c")


elif (b==c) and (b>a):
    print("b=c greater a")

elif (a==c) and (a>b):
    print("a=c greater b")
else:
    print("They are equal")


"""The purpose of this code is to see how the "and" logical operator comes in,
Its main use is to compare two operators 'or is for one operator and 'not' showing an operator is not equal to zero'"""


