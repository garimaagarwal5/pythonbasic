'''
Raining like cats and dogs
● Take user input in the form of a string.
● Return True if the string "cat" and "dog" appear the same number of times
in the given string
● file name must be lnbcatndog.py in which you are writing code
● commit this code on your github link under pythonstring branch
'''
def funccount(str):
    if str.count('cat')== str.count('dog'):#number of count of cat is equal to number of count of dog
        return True
    else:
        return False
    
str=input("enter a string in cat dog form")
print(funccount(str))#call function funccount