#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[9]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print(f'{match}')


# # Q2

# In[19]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
# print(len(text))
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(f'Found "%s" at %d:%d' % (text[s:e], s, e))
#The finditer function of the regex library can help us perform the task of finding the
#occurrences of the substring in the target string and the start function can return the 
#resultant index of each of them.


# # Q3

# In[21]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)


# In[17]:


s = 'this is an __example__'
translate_table = str.maketrans({' ': '_', '_': ' '})
print(s.translate(translate_table))


# In[22]:


import re

my_str = 'one    two   three'

result = re.sub(r"\s+", '-', my_str)

print(result)


# # Q4

# In[27]:


import re
def extract_date(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))


# # Q5

# In[25]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# # Q6

# In[3]:


import re
# Sample strings.
words = ['Python php',' exercises', 'PHP', 'C# exercises','Python.php']
for w in words:
    m = re.findall('(P\w+)\W(P\w+)', w)
    if m:
        print(m)


# # Q7

# In[5]:


import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
# Print results.
for element in result:
    print(element)


# In[6]:


import re
# Sample string.
text = "Ten 10, Twenty 20, Thirty 30"
result = re.findall("\d+", text)
# Print results.
for element in result:
    print(element)


# # Q8

# In[7]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)


# # Q9

# In[13]:


import re
# Input.
text = "2The following example creates an ArrayList with 60 a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# print(len(text))
for m in re.finditer("\d+", text):
    print(m.group())
    s=m.start()
    e=m.end()
    print("Index position:", s, e)


# # Q10

# In[28]:


import re
street = '21 RoadRamkrishna Road'
print(re.sub('Road', 'Rd.', street))


# In[27]:


import re
street = '21 RoadRamkrishna Road'
print(re.sub('Road$', 'Rd.', street))


# In[29]:


import re
street = '21 Road Ramkrishna Road'
print(re.sub('Road$', 'Rd.', street))


# In[30]:


import re
street = '21 Road Ramkrishna Road'
print(re.sub('Road', 'Rd.', street))


# In[57]:


#Q2 
import re

class User:
    def __init__(self, f_name, l_name, user_name, password, phone, email):
        self.f_name=f_name
        self.l_name=l_name
        self.user_name=user_name
        self.__password=password
        self.phone=phone
        self.email=email
        self.user_info={}
        
    def register(self):
        self.validate()
        if self.user_name in self.user_info:
            raise Exception("Account already exist!!")
        else:
            self.user_info.update ({self.user_name:[self.__password, self.f_name, self.l_name, self.phone, self.email]})
    
    def validate(self):
        assert re.findall('^(\+98)?9\d{9}$' , self.phone),'invalid phone'
        assert re.findall('[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' , self.email), 'invalid email'
        assert re.findall('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$' , self.__password) ,'invalid password'
        
        return True
    
    def login(self, user_name, password):
        if self.user_name in self.user_info:
            if self.__password==password:
                return True
            return False
        return 'user did not sign up yet'
    
class Main:
    try:
        obj = User("zahra", "Rezaei", "szrezaei", "12345", "+989121234567", "zahra.example@gmail.com")
        obj.register()
        print(obj.login("szrezaei", "12345"))
        print(obj.login("reza", "12345"))
        print(obj.login("szrezaei", "09867"))
    except AssertionError as msg:
        print(msg)    


# In[5]:


import re


class User:
    def __init__(self, f_name, l_name, user_name, password, phone, email):
        self.f_name = f_name
        self.l_name = l_name
        self.user_name = user_name
        self.__password = password
        self.phone = phone
        self.email = email
        self.user_info = {}

    def register(self):
        self.validate()
        if self.user_name in self.user_info:
            raise Exception("Account already exist!!")
        else:
            self.user_info.update({self.user_name: [self.__password, self.f_name, self.l_name, self.phone, self.email]})

    def validate(self):
        assert re.findall("^(\+98)?9\d{9}$", self.phone), "invalid phone number!"
        assert re.findall("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", self.email), "invalid email!"
        assert re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", self.__password), "invalid password!"

        return True

    def login(self, username, password):
        if username in self.user_info:
            if self.__password == password:
                return "Successfully"
            else:
                return "Wrong password!"
        else:
            return "This user has not registered!"


class Main:
    try:
        obj = User("zahra", "Rezaei", "szrezaei", "12345", "+9891212345", "zahra.example@")
        obj.register()
        print(obj.login("szrezaei", "12345"))
        print(obj.login("zednun", "12345"))
        print(obj.login("szrezae", "1234598"))
    except AssertionError as msg:
        print(msg)


# In[ ]:




