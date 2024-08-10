#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1 to 10 natural numbers
for i in range(1,11):
    print(i)


# In[4]:


#sum of numbers from 1 to 10
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)


# In[6]:


list=[1,2,3,4,5,6,7,8,9]
for i in list:
    print(i)


# In[12]:


#product of elements in the list
list=[1,2,3]
product=1
for i in list:
    product=product*i
print(product)


# In[15]:


#even numbers from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)


# In[19]:


for i in range(2,11,2):   #1,2,3,4,5,6,7,8,9,10
    print(i)


# In[22]:


#print 1 to 10 in reverse order
list=[10,9,8,7,6,5,4,3,2,1]
for i in list:
    print(i)


# In[24]:


for i in range(10,0,-1):
    print(i)


# In[37]:


#print characters of a string
a="abcdef"
for i in a:
    print(i)


# In[43]:


list=[1,2,3,4,5]
largest=list[0]
for num in list:
    if num<largest:
        largest=num
print(largest)


# In[44]:


#print largest number of a list
list=[2,7,3,9,11,14,16]
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print(largest)


# In[51]:


#average number in a list
list=[10,20]
sum=0
for num in list:
    sum=sum+num
avg=sum/2
print(avg)
    


# In[55]:


#print all uppercase letters of a strings
a="AbCdFR"
for i in a:
    if i.isupper():
        print(i)
    


# In[56]:


#count no of vowels in a string
vowels="AEIOUaeiou"
count=0
string="abce"
for char in string:
    if char in vowels:
        count=count+1
print(count)
        


# In[69]:


for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()


# In[ ]:




