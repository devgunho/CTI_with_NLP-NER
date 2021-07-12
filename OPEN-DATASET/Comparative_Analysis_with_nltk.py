#%%
import json

#%%
with open("../dataset/dictionary.json", "r", encoding="utf-8") as f:
    dic_data = json.load(f)

print("[*] Print dic_data :", dic_data[0])
print("[*] Total Corpus :", len(dic_data))

#%%
#========== data.adj ==========
with open("./NLTK-DATA/data.adj", "r", encoding="utf-8") as f:
    adj_data = f.readlines()

print("[*] Print adj_data :", type(adj_data), "/", len(adj_data))
print("[*] Print adj_data[0] :", adj_data[0])

#%%
adjs = []
adj_collision = []
counter = 0
for line in adj_data:
    counter += 1
    token = (line.split()[4])
    adjs.append(token)

    for i in dic_data:
        if token == i['corpus'].lower():
            adj_collision.append(token)
            print("Verification Required :", token)

    print("NOW / Total :", len(adjs), '-', token, "\t/", len(adj_data),
          "| Collision :", len(adj_collision))

# %%
print(adj_collision)
with open('adj_result.txt', 'w', newline='') as file:
    file.write(str(adj_collision))

#%%
#========== data.adv ==========
with open("./NLTK-DATA/data.adv", "r", encoding="utf-8") as f:
    adv_data = f.readlines()

print("[*] Print adv_data :", type(adv_data), "/", len(adv_data))
print("[*] Print adv_data[0] :", adv_data[0])

# %%
advs = []
adv_collision = []
counter = 0
for line in adv_data:
    counter += 1
    token = (line.split()[4])
    advs.append(token)

    for i in dic_data:
        if token == i['corpus'].lower():
            adv_collision.append(token)
            print("Verification Required :", token)

    print("NOW / Total :", len(advs), '-', token, "\t/", len(adv_data),
          "| Collision :", len(adv_collision))

# %%
print(adv_collision)
with open('adv_result.txt', 'w', newline='') as file:
    file.write(str(adv_collision))

#%%
#========== data.noun ==========
with open("./NLTK-DATA/data.noun", "r", encoding="utf-8") as f:
    noun_data = f.readlines()

print(type(noun_data), "/", len(noun_data))
print(noun_data[0])

# %%
nouns = []
noun_collision = []
counter = 0
for line in noun_data:
    counter += 1
    token = (line.split()[4])
    nouns.append(token)

    for i in dic_data:
        if token == i['corpus'].lower():
            noun_collision.append(token)
            print("Verification Required :", token)

    print("NOW / Total :", len(nouns), '-', token, "\t/", len(noun_data),
          "| Collision :", len(noun_collision))

# %%
with open('noun_result.txt', 'w', newline='') as file:
    file.write(str(noun_collision))

#%%
#========== data.verb ==========
with open("./NLTK-DATA/data.verb", "r", encoding="utf-8") as f:
    verb_data = f.readlines()

print(type(verb_data), "/", len(verb_data))
print(verb_data[0])

# %%
verbs = []
verb_collision = []
counter = 0
for line in verb_data:
    counter += 1
    token = (line.split()[4])
    verbs.append(token)

    for i in dic_data:
        if token == i['corpus'].lower():
            verb_collision.append(token)
            print("Verification Required :", token)

    print("NOW / Total :", len(verbs), '-', token, "\t/", len(verb_data),
          "| Collision :", len(verb_collision))

# %%
with open('verb_result.txt', 'w', newline='') as file:
    file.write(str(verb_collision))
