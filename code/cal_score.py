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
csv_file_train=pd.read_csv('../data/test_a.csv')

def cal_score(df_predict):
    y_real=df_predict['tradeMoney'].tolist()
    y_predict=[0 for i in range(len(y_real))]
    m=len(y_real)
    y_average=np.mean(np.array(y_real))
    sum_fz=0
    sum_fm=0
    for i in range(m):
        sum_fz+=(y_predict[i]-y_real[i])**2
        sum_fm+=(y_real[i]-y_average)**2
    score=1-sum_fz/sum_fm
    return score

score=cal_score(csv_file_train)
print(score)


# In[ ]:




