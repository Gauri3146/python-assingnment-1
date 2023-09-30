#!/usr/bin/env python
# coding: utf-8

# In[5]:


scores=[35,50,20,30,55,75,90,95,66,80]
for i in scores:
    if i>70:
        print("Distinction")
    elif 60<i<70:
        print("First Class")
    elif 50<i<60:
        print("Second Class")
    elif 35<i<50:
        print("Just Pass")
    else:
        print("Fail")


# In[7]:


Book_price= {'Python':600, 'Java': 400, 'Web_Tech': 550, 'OS': 450, 'IT': 700}
for x,y in Book_price.items():
    if y>500:
        print(x)


# In[8]:


aList = [1, 2, 3, 4, 5, 6, 7]
squared_list=[i**2 for i in aList]
squared_list


# In[13]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        print(i+j)


# In[14]:


aLsit = [100, 200, 300, 400, 500]
rev=aLsit[::-1]
rev


# In[15]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
list1


# In[1]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i","j"])
list1


# In[2]:


list1=[5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
list1


# In[4]:


Player_game={'Sachin':'Cricket', 'Rahul': 'Cricket', 'Messi': 'Football', 'Federer': 'Tennis', 'Anand': 'Chess'}
for x,y in Player_game.items():
    if y=='Cricket':
        print(x)


# In[6]:


Sum=0
List1= [1,2,4,5,10,20,4,5]
for i in List1:
    Sum+=i
Sum


# In[ ]:




