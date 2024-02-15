'''
Take User input and decode logic
● Take 2 integer input from user and print their products(their multiplication)
● IF product is greater than 500 then return their sum
● If the product is smaller than 500 then return "Hello LNB code is running
fine !!"
● file name must be lnbcal.py in which you are writing code
● commit this code on your github link under pythonbasic branch

'''
def func1(a,b):
    prod_of_a_and_b=a*b
    if prod_of_a_and_b>500:#check product of a and b
        return a+b#return sum of a and b
    else:
        return "Hello LNB code's running fine"#return this message
    
a=int(input("enter a number a"))
b=int(input("enter a number b"))
print(func1(a,b))#call function func1