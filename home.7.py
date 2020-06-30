#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.printing integers from 1 to 100
ints=[]
for i in range(1,101):
    if i%3==0 and i%5==0:
        ints.append('FizzBuzz')
        continue
    elif i%3==0:
        ints.append('Fizz')
        continue
    elif i%5==0:
        ints.append('Buzz')
        continue
    else:
        ints.append(i)
        continue
print(ints)


# In[ ]:


#2.removing consecutive duplicates from a list
a=(1,1,1,2,2,2,3,3,3)
b=[]
for i in a:
    if i not in b:
        b.append(i)
        continue
print(b)


# In[ ]:


#3.finding a unique element from a given list
a=input("enter the list : ")
b=input("enter the element : ")
i=0
for i in range(len(a)):
    if a[i] == b:
        print("element found at index : ",(i-2))
        break
    else:
        continue


# In[ ]:


#4.finding whether a given number is within range
def test_range(a,b,n):
    if n in range(a+1,b):
        print("%s is in range"%str(n))
    else:
        print("%s is not in given range"%str(n))
n=int(input("enter the number : "))
a=int(input("enter the lower limit : "))
b=int(input("enter the upper limit : "))
test_range(a,b,n)


# In[ ]:


#5.calculating no. of uppercase and lowercase letters in a string
a=input("enter the string : ")
count1=0
count2=0
for i in a:
    if (i.isupper()):
        count1=count1+1
    elif (i.islower()):
        count2=count2+1
print("the no. of uppercase letters is : ",count1)
print("the no. of lowercase letters is : ",count2)


# In[ ]:




