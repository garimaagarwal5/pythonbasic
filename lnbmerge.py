'''14. MAKE A PROGRAM TO MERGE TWO LIST INTO A
SINGLE DICTIONARIES
● Take inputs from the user
● Any one list must contain unique elements
● both the list should be of the same size
● both the list should be a combination of numbers and names
● Name of dictionary you can take it accordingly
● file name should be in lnbmerge.py
● commit the code on github link under pythonbasic branch '''

k1=[input("enter names ") for i in range(3)]#create a list k1
val1=[input("enter  address") for j in range(3)]#create a list val1
d={}#create a dictionary
for k in k1:#traversing a list k1
    for val in val1:#traversing a list val1
        d[k]=val#assignment of keys and values in dictionary
print(d)