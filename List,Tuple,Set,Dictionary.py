#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Variable input
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
z=x+y
print(z)


# In[7]:


k=("Hello world")
print(k[1])
print(k[2])
print(k[0:2])


# In[8]:


#list
list=["uba","tamim","shohel","shovon"]
list[3]="sunny"
list.insert(3,"monir")
list.append("mohitun")
list.remove("tamim")
print(list)
print(list[2])
print(list[1:3])
list.sort()
print(list)
list3=list.copy()
print(list3)
list.extend(list3)
print(list)
print("uba" in list)
for x in list:
    print(list)


# In[16]:


#tuple
tuple=("uba","tamim","shohel","robiul")
print(tuple)
print(len(tuple))
print(tuple[2])
print(tuple[1:3])
print(tuple)
tuple=tuple*2
print(tuple)


# In[13]:


#set
set={"crow","tamim",34, "True", 40}

print(set)
set.add("uba")
print(set)
for x in set:
    print(x)
    
#new set(union)    
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


# In[28]:


#Dictionary
dict1= {
    "brand":"realme",
    "model":"C51",""
    "year":2023
}
print(dict1)

dict2= {
    "brand":"realme",
    "model":"C53",
    "year":2023

}
print(dict2)
print(dict2["brand"])
print(dict2["model"])
dict2.update({"year":2022})
print(dict2)

