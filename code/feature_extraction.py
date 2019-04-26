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
    df_ret = df_origin
    dict_commnityname_trademoney = {}
    for i in df_ret['communityName'].unique():
        trademoney_ave = df_ret[df_ret['communityName'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_ret.iterrows():
        communityname = row['communityName']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'community_ave_trademoney': list_trademoney_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret


def add_region_ave_trademoney(df_origin):
    df_ret = df_origin
    dict_commnityname_trademoney = {}
    for i in df_ret['region'].unique():
        trademoney_ave = df_ret[df_ret['region'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_ret.iterrows():
        communityname = row['region']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'region_ave_trademoney': list_trademoney_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret


def add_plate_ave_trademoney(df_origin):
    df_ret = df_origin
    dict_commnityname_trademoney = {}
    for i in df_ret['plate'].unique():
        trademoney_ave = df_ret[df_ret['plate'] == i]['tradeMoney'].mean()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_ret.iterrows():
        communityname = row['plate']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'plate_ave_trademoney': list_trademoney_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret


def add_pv_div_uv(df_origin):
    df_ret = df_origin
    list_pv_div_uv = []
    for index, row in df_ret.iterrows():
        pv = row['pv']
        uv = row['uv']
        pv_div_uv = float(pv) / float(uv)
        list_pv_div_uv.append(pv_div_uv)
    dict_pv_div_uv = {'pv_div_uv': list_pv_div_uv}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_pv_div_uv)], axis=1)
    return df_ret


def add_month_ave_trademoney(df_origin):
    df_ret = df_origin
    dict_month_ave_money = {}
    for i in df_ret['tradeMonth'].unique():
        trademoney_ave = df_ret[df_ret['tradeMonth'] == i]['tradeMoney'].mean()
        dict_month_ave_money[i] = trademoney_ave
    list_trademoney_month_ave = []
    for index, row in df_ret.iterrows():
        month = row['tradeMonth']
        trademoney = dict_month_ave_money[month]
        list_trademoney_month_ave.append(trademoney)
    dict_trademoney_final = {'month_ave_trademoney': list_trademoney_month_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret


def add_totalfloor_times_housefloor(df_origin):
    df_ret = df_origin
    list_totalfloor_times_housefloor = []
    for index, row in df_ret.iterrows():
        housefloor = row['houseFloor']
        totalfloor = row['totalFloor']
        if housefloor == 0:
            ratio = 0.5
        elif housefloor == 1:
            ratio = 1.5
        else:
            ratio = 2.5
        list_totalfloor_times_housefloor.append(ratio * totalfloor)
    dict_totalfloor_times_housefloor = {'totalfloor_times_housefloor': list_totalfloor_times_housefloor}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_totalfloor_times_housefloor)], axis=1)
    return df_ret


def add_housetype_to_num(df_origin):
    df_ret = df_origin
    list_num = []
    for index, row in df_ret.iterrows():
        bedroom = row['bedroom']
        livingroom = row['livingroom']
        bathroom = row['bathroom']
        num = 14 * bedroom + 14 * livingroom + 3 * bathroom
        list_num.append(num)
    dict_num = {'housetype_to_num': list_num}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_num)], axis=1)
    return df_ret


def add_tradeyear_minus_buildyear(df_origin):
    df_ret = df_origin
    list_year = []
    for index, row in df_ret.iterrows():
        buildyear = row['buildYear']
        tradeyear = row['tradeYear']
        list_year.append(tradeyear - buildyear)
    dict_year = {'tradeyear_minus_buildyear': list_year}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_year)], axis=1)
    return df_ret


def add_plate_num_in_region(df_origin):
    df_ret = df_origin
    dict_plate_num = {}
    list_region = list(df_ret['region'].unique())
    list_plate_num_in_region = []
    for region in list_region:
        plate_num = len(df_ret[df_ret['region'] == region]['plate'].unique())
        dict_plate_num[region] = plate_num
    for index, row in df_ret.iterrows():
        region = row['region']
        plate_num = dict_plate_num[region]
        list_plate_num_in_region.append(plate_num)
    dict_plate_num_in_region = {'plate_num_in_region': list_plate_num_in_region}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_plate_num_in_region)], axis=1)
    return df_ret


def add_community_num_in_plate(df_origin):
    df_ret = df_origin
    dict_community_num = {}
    list_plate = list(df_ret['plate'].unique())
    list_community_num_in_plate = []
    for plate in list_plate:
        community_num = len(df_ret[df_ret['plate'] == plate]['communityName'].unique())
        dict_community_num[plate] = community_num
    for index, row in df_ret.iterrows():
        plate = row['plate']
        community_num = dict_community_num[plate]
        list_community_num_in_plate.append(community_num)
    dict_community_num_in_plate = {'community_num_in_plate': list_community_num_in_plate}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_community_num_in_plate)], axis=1)
    return df_ret


def add_transport_total_num(df_origin):
    df_ret = df_origin
    list_transport_total_num = []
    for index, row in df_ret.iterrows():
        subway_num = row['subwayStationNum']
        bus_num = row['busStationNum']
        total_num = subway_num + bus_num
        list_transport_total_num.append(total_num)
    dict_transport_total_num = {'transport_total_num': list_transport_total_num}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_transport_total_num)], axis=1)
    return df_ret


def add_education_total_num(df_origin):
    df_ret = df_origin
    list_education_total_num = []
    for index, row in df_ret.iterrows():
        interschool_num = row['interSchoolNum']
        school_num = row['schoolNum']
        privateschool_num = row['privateSchoolNum']
        total_num = interschool_num + school_num + privateschool_num
        list_education_total_num.append(total_num)
    dict_transport_total_num = {'education_total_num': list_education_total_num}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_transport_total_num)], axis=1)
    return df_ret


def add_service_total_num(df_origin):
    df_ret = df_origin
    list_service_total_num = []
    for index, row in df_ret.iterrows():
        hospital_num = row['hospitalNum']
        drugstore_num = row['drugStoreNum']
        gym_num = row['gymNum']
        bank_num = row['bankNum']
        shop_num = row['shopNum']
        park_num = row['parkNum']
        mall_num = row['mallNum']
        supermarket_num = row['superMarketNum']
        total_num = hospital_num + drugstore_num + gym_num + bank_num + shop_num + park_num + mall_num + supermarket_num
        list_service_total_num.append(total_num)
    dict_service_total_num = {'service_total_num': list_service_total_num}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_service_total_num)], axis=1)
    return df_ret


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
