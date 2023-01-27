#!/usr/bin/env python
# coding: utf-8

# In[2]:


import psycopg2
import pandas as pds
import pandas.io.sql as sqlio


# In[18]:


#connect to potsgresql
try:
  conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
  print("connnection success")
except:
  print("An exception occurred")


# In[19]:


#with cursor
cur = conn.cursor()
cur.execute('Select * from public.kelas')

#showing result
one = cur.fetchone()
all = cur.fetchall()
conn.commit()

print(one)

for record in all:
    print(str(record[0]) +"-"+ record[1])
    
data = sqlio.read_sql_query("Select * from public.kelas", conn)
# Now data is a pandas dataframe having the results of above query.
data.head()

#print(one);


# In[ ]:





# In[ ]:




