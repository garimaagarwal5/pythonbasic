'''List operations and decoding
● two lists are given below L1, L2.
● create a new list called L3 containing items in below given pattern
● From L1 it must take only odd index items
● From L2 it must take only even index items
● file name must be lnblist.py in which you are going to write the code
● commit this code on your github link under pythonbasic branch'''
l1=[]
l2=[]
l3=[]
for i in range(5):
    num=int(input("enter a number in list1"))
    l1.append(num)
for i in range(1,6):
    num=int(input("enter a number in list 2"))
    l2.append(num)
for i in range(1,len(l1)):
    if i %2!=0:
        print(f"odd index {i}")
        l3.append(l1[i])
for j in range(1,len(l2)):
    if j %2==0:
        print(f"even index{j}")
        l3.append(l2[j])
print(l3)


