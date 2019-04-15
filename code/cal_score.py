#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


csv_file_train=pd.read_csv('train_data.csv')
csv_file_test=pd.read_csv('test_a.csv')


# In[3]:


csv_file_train.info()


# In[11]:


import numpy as np
csv_file_train=pd.read_csv('train_data.csv')
y_real=csv_file_train['tradeMoney'].tolist()
y_predict=[0 for i in range(len(y_real))]

def cal_score(y_real,y_predict):
    y_r=np.array(y_real)
    y_p=np.array(y_predict)
    m=len(y_real)
    y_average=np.mean(y_r)
    sum_fz=0
    sum_fm=0
    for i in range(m):
        sum_fz+=(y_predict[i]-y_real[i])**2
        sum_fm+=(y_real[i]-y_average)**2
    score=1-sum_fz/sum_fm
    return score
score=cal_score(y_real,y_real)
print(score)


# In[ ]:




