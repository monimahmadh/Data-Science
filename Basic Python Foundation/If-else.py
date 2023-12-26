#!/usr/bin/env python
# coding: utf-8

# In[5]:


#if-else 

x=int(input("Enter x value : "))
y=int(input("Enter y value : "))
if x>y:
    print("X is Bigger than Y")
elif x==y:
    print("X is equal to Y")
else:
    print("Y is Bigger than X")


# In[6]:


#write a program of grading system using if-else
x=int(input("Enter x value : "))
if 100>=x>=80:
    print("A+")
elif 79>=x>=70:
    print("A")
elif 69>=x>=60:
    print("A-")
elif 59>=x>=50:
    print("B")
elif 49>=x>=40:
    print("C")
elif 39>=x>=33:
    print("D")
else:
    print("Fail")


# In[ ]:




