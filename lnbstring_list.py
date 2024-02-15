'''
13. Paragraph to list
● Take input from the user in string form(a sentence or para)
● All the words in the string having more than 4 letters should be stored in a
list
● file name must be lnbstring_list.py in which you are writing code.
● commit this code on your github link under pythonbasic branch
Sample Input : A paragraph is defined as “a group of sentences or a single sentence
that forms a unit”. Length and appearance do not determine whether a section in a
paper is a paragraph.
'''
str=input("enter a string").split()#take input from user
l=[]#create a list
for s in str:#traversing a list
    if len(s)>4:#check length of each string in sentence
        l.append(s)
print(l)