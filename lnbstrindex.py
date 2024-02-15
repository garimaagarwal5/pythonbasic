'''Take User input in string form and perform operation
● Take input from user in string form only and calculate the length of string
● IF length is greater than 7 then display only those character which are
present in even index number
● if length is less than or equals to 7 then display only those character which
are present in odd index number
● file name must be lnbstrindex.py in which you are writing code
● commit this code on your github link under pythonbasic branch'''
str=input("enter a string")
len_of_str=len(str)

if len_of_str>7:
    print(str[0:len_of_str:2])#print even index postion characters
else:
    print(str[1:len_of_str:2])#print odd index characters
