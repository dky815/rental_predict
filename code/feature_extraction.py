# -*- coding: utf-8 -*-

import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

import numpy as np

df_processed = pd.read_csv('/content/gdrive/My Drive/data_processed.csv')

df_processed['houseToward'] = df_processed['houseToward'].astype('category')
df_processed['rentType'] = df_processed['rentType'].astype('category')
df_processed['houseDecoration'] = df_processed['houseDecoration'].astype('category')
df_processed['houseFloor'] = df_processed['houseFloor'].astype('category')
df_processed['communityName'] = df_processed['communityName'].astype('category')
df_processed['region'] = df_processed['region'].astype('category')
df_processed['plate'] = df_processed['plate'].astype('category')

df_processed = df_processed.drop(columns=['tradeYear'])


def add_community_ave_trademoney(df_origin):
    df_processed = df_origin
    dict_commnityname_trademoney = {}
    for i in df_processed['communityName'].unique():
        trademoney_ave = df_processed[df_processed['communityName'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_processed.iterrows():
        communityname = row['communityName']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'community_ave_trademoney': list_trademoney_ave}
    df_processed = pd.concat([df_processed, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_processed


def add_region_ave_trademoney(df_origin):
    df_processed = df_origin
    dict_commnityname_trademoney = {}
    for i in df_processed['region'].unique():
        trademoney_ave = df_processed[df_processed['region'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_processed.iterrows():
        communityname = row['region']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'region_ave_trademoney': list_trademoney_ave}
    df_processed = pd.concat([df_processed, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_processed


def add_plate_ave_trademoney(df_origin):
    df_processed = df_origin
    dict_commnityname_trademoney = {}
    for i in df_processed['plate'].unique():
        trademoney_ave = df_processed[df_processed['plate'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_processed.iterrows():
        communityname = row['plate']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'plate_ave_trademoney': list_trademoney_ave}
    df_processed = pd.concat([df_processed, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_processed


def add_pv_div_uv(df_origin):
    df_processed = df_origin
    list_pv_div_uv = []
    for index, row in df_processed.iterrows():
        pv = row['pv']
        uv = row['uv']
        pv_div_uv = float(pv) / float(uv)
        list_pv_div_uv.append(pv_div_uv)
    dict_pv_div_uv = {'pv_div_uv': list_pv_div_uv}
    df_processed = pd.concat([df_processed, pd.DataFrame(dict_pv_div_uv)], axis=1)
    return df_processed


def add_month_ave_trademoney(df_origin):
    df_processed = df_origin
    dict_month_ave_money = {}
    for i in df_processed['tradeMonth'].unique():
        trademoney_ave = df_processed[df_processed['tradeMonth'] == i]['tradeMoney'].mean()
        dict_month_ave_money[i] = trademoney_ave
    list_trademoney_month_ave = []
    for index, row in df_processed.iterrows():
        month = row['tradeMonth']
        trademoney = dict_month_ave_money[month]
        list_trademoney_month_ave.append(trademoney)
    dict_trademoney_final = {'month_ave_trademoney': list_trademoney_month_ave}
    df_processed = pd.concat([df_processed, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_processed


def test_feature(df_origin, feature_function, y_predict):
    df_test = df_origin.copy()
    df_test = feature_function(df_test)
    return test_score(df_test, y_predict)


def test_score(df_test, y_predict):
    y_real = df_test.tolist()
    m = len(y_real)
    y_average = np.mean(np.array(y_real))
    sum_fz = 0
    sum_fm = 0
    for i in range(m):
        sum_fz += (y_predict[i] - y_real[i]) ** 2
        sum_fm += (y_real[i] - y_average) ** 2
    score = 1 - sum_fz / sum_fm
    return score


X = df_processed.drop(columns=['tradeMoney'])
y = df_processed['tradeMoney']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model_lgb = lgb.LGBMRegressor(objective='regression', num_leaves=900, device="gpu",
                              learning_rate=0.1, n_estimators=3141, bagging_fraction=0.7,
                              feature_fraction=0.6, reg_alpha=0.3, reg_lambda=0.3,
                              min_data_in_leaf=18, min_sum_hessian_in_leaf=0.001)
model_lgb.fit(X_train, y_train)
predict = model_lgb.predict(X_test)
print(test_score(y_test, predict))



# predict=predict.T
# predict_df=pd.DataFrame(predict)
# predict_df.to_csv('pre_df.csv', encoding='utf-8', index=False)
# pre_df=pd.read_csv('pre_df.csv')
