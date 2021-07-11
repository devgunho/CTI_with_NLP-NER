# In[1]:


import json
import pandas as pd

with open("../dataset/dictionary.json", "r", encoding="utf-8") as f:
    dic_data = json.load(f)

print(dic_data[0])


# In[2]:


print("Total Corpus :", len(dic_data))


# In[1]:


with open("./NLTK-DATA/data.adj", "r", encoding="utf-8") as f:
    adj_data = f.readlines()

print(type(adj_data), "/", len(adj_data))
print(adj_data[0])


# In[ ]:


adjs = []
for line in adj_data:
    token = (line.split()[4])
    adjs.append(token)
print(len(adjs))


# In[4]:


with open("./NLTK-DATA/data.adv", "r", encoding="utf-8") as f:
    adv_data = f.readlines()

print(type(adv_data), "/", len(adv_data))
print(adv_data[0])


# In[5]:


with open("./NLTK-DATA/data.noun", "r", encoding="utf-8") as f:
    noun_data = f.readlines()

print(type(noun_data), "/", len(noun_data))
print(noun_data[0])


# In[6]:


with open("./NLTK-DATA/data.verb", "r", encoding="utf-8") as f:
    verb_data = f.readlines()

print(type(verb_data), "/", len(verb_data))
print(verb_data[0])
