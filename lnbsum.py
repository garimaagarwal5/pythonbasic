'''
1. Take User input and process
● Take 5 integer input from the user.
● Remove all numbers less than 9.
● Calculate the sum of remaining numbers
● File name must be lnbsum.py in which you are writing code
● Commit this code on your github link under pythonbasic branch
'''
#get input from user
li=[]
for i in range(5):#loop to enter a number into list
    li.append(int(input("enter a number")))
print(f'''the list is
      {li}''')
li=list(filter(lambda x:x>9,li))#filters numbers greater than 9 in new list
print(f"now the updated list is {li} ")#updated list
total=0 

for i in li:
    total=total+i
print(f"the sum of list of numbers is {total}")
