'''Splitting the list
● Create a list ranging from 1-20
● Create a new list that contains first and the last five elements of the
existing list
● Now create and display another list that contains square of the elements
of the new list
● Now split the new list into three parts where the length of splitted parts
should be two, three and five respectively
● File name must be in lnblist.py in which you are writing code
● Commit this code on your github link under the python string branch'''

l1=[int(input("enter a number")) for i in range(20)]#create a list
l2=l1[0:5]#sublist containing first five numbers
l3=l1[15:20]#sublist containing last five numbers
l4=l2+l3#joining of two list
print(l4)
l4=[i**2 for i in l4]#square of a list l4
print(l4)
newl1=l4[0:2]#containing two numbers
newl2=l4[2:5]#containing three numbers
newl3=l4[5:10]#containing five numbers
print(newl1)
print(newl2)
print(newl3)


