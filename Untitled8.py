
# coding: utf-8

# In[37]:


def find_longest_term(word_list):
    word_length = []
    for i in word_list:
        word_length.append((len(i),i))
    word_length.sort()
    return word_length[-1][1]


# In[38]:


x = find_longest_term(["hyderabad","mumbai","chennai"])


# In[39]:


print(x)

