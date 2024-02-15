'''10. Convert tuple to list using given string
● Take input from the user in the form of tuple
● Take another input from the user in the form of string
● Convert the tuple to list
● Add string to the list after each element
● Convert list to tuple again
● File name must be lnbconvtuple.py in which you are writing the code
● Commit this code on your github link under pythonbasic branch'''

t=tuple(input("enter a words separated by ,").split(','))
str=input("enter a string")
l=list(t)
for i in range(len(l)):
    l[i]=l[i]+','+str
print("list is",l)
t=tuple(l)
print(t)