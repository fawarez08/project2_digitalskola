#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur  = conn.cursor()

with open('C:/Users/Reza Fawazul/.vscode/project3_batchprocessing/source/users_w_postal_code.csv','r') as f:
    next(f)
    cur.copy_from(f,'latihan_users',sep=',',columns=('email','name','phone','postal_code'))
conn.commit()


# In[ ]:




