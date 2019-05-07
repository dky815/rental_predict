import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def add_community_ave_trademoney(df_origin):
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
    list_year = []
    tradeyear=2018
    list_buildyear = df_ret['buildYear'].tolist()
    for buildyear in list_buildyear:
        list_year.append(tradeyear - buildyear)
    dict_year = {'tradeyear_minus_buildyear': list_year}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_year)], axis=1)
    return df_ret


def add_plate_num_in_region(df_origin):
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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
    df_ret = df_origin.copy()
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


def test_feature(df_origin, feature_function):
    df_test = df_origin.copy()
    df_test = feature_function(df_test)
    X = df_test.drop(columns=['tradeMoney'])
    y = df_test['tradeMoney'].tolist()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    model_lgb = lgb.LGBMRegressor(objective='regression', num_leaves=900,
                                  learning_rate=0.1, n_estimators=3141, bagging_fraction=0.7,
                                  feature_fraction=0.6, reg_alpha=0.3, reg_lambda=0.3,
                                  min_data_in_leaf=18, min_sum_hessian_in_leaf=0.001)
    model_lgb.fit(X_train, y_train)
    y_predict = model_lgb.predict(X_test)
    if len(y_test)==len(y_predict):
        return test_score(y_test, y_predict)
    else:
        print("len ytest != len ypredict")
        return


def test_score(y_real, y_predict):
    m = len(y_real)
    y_average = np.mean(np.array(y_real))
    sum_fz = 0
    sum_fm = 0
    for i in range(m):
        sum_fz += (y_predict[i] - y_real[i]) ** 2
        sum_fm += (y_real[i] - y_average) ** 2
    score = 1 - sum_fz / sum_fm
    return score


def add_lookNum_div_pv(df_origin):
    df_ret=df_origin.copy()
    list_lookNum_div_pv=[]
    for index,row in df_ret.iterrows():
        lookNum=row['lookNum']
        pv=row['pv']
        lookNum_div_pv=float(lookNum)/float(pv)
        list_lookNum_div_pv.append(lookNum_div_pv)
    dict_lookNum_div_pv={'lookNum_div_pv':list_lookNum_div_pv}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_lookNum_div_pv)],axis=1)
    return df_ret

def add_lookNum_div_uv(df_origin):
    df_ret=df_origin.copy()
    list_lookNum_div_uv=[]
    for index,row in df_ret.iterrows():
        lookNum=row['lookNum']
        uv=row['uv']
        lookNum_div_uv=float(lookNum)/float(uv)
        list_lookNum_div_uv.append(lookNum_div_uv)
    dict_lookNum_div_uv={'lookNum_div_uv':list_lookNum_div_uv}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_lookNum_div_uv)],axis=1)
    return df_ret

def add_totalWorkers_div_residentPopulation(df_origin):
    df_ret=df_origin.copy()
    list_totalWorkers_div_residentPopulation=[]
    for index,row in df_ret.iterrows():
        totalWorkers=row['totalWorkers']
        residentPopulation=row['residentPopulation']
        totalWorkers_div_residentPopulation=float(totalWorkers)/float(residentPopulation)
        list_totalWorkers_div_residentPopulation.append(totalWorkers_div_residentPopulation)
    dict_totalWorkers_div_residentPopulation={'totalWorkers_div_residentPopulation':list_totalWorkers_div_residentPopulation}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_totalWorkers_div_residentPopulation)],axis=1)
    return df_ret

def add_newWorkers_div_totalWorkers(df_origin):
    df_ret=df_origin.copy()
    list_newWorkers_div_totalWorker=[]
    for index,row in df_ret.iterrows():
        newWorkers=row['newWorkers']
        totalWorker=row['totalWorkers']
        newWorkers_div_totalWorker=float(newWorkers)/float(totalWorker)
        list_newWorkers_div_totalWorker.append(newWorkers_div_totalWorker)
    dict_newWorkers_div_totalWorker={'newWorkers_div_totalWorker':list_newWorkers_div_totalWorker}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_newWorkers_div_totalWorker)],axis=1)
    return df_ret

def add_tradeLandArea_div_tradeLandNum(df_origin):
    df_ret=df_origin.copy()
    list_tradeLandArea_div_tradeLandNum=[]
    for index,row in df_ret.iterrows():
        tradeLandArea=row['tradeLandArea']
        tradeLandNum=row['tradeLandNum']
        if tradeLandNum==0:
            list_tradeLandArea_div_tradeLandNum.append(0)
            continue
        tradeLandArea_div_tradeLandNum=float(tradeLandArea)/float(tradeLandNum)
        list_tradeLandArea_div_tradeLandNum.append(tradeLandArea_div_tradeLandNum)
    dict_tradeLandArea_div_tradeLandNum={'tradeLandArea_div_tradeLandNum':list_tradeLandArea_div_tradeLandNum}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_tradeLandArea_div_tradeLandNum)],axis=1)
    return df_ret

def add_supplyLandArea_div_supplyLandNum(df_origin):
    df_ret=df_origin.copy()
    list_supplyLandArea_div_supplyLandNum=[]
    for index,row in df_ret.iterrows():
        supplyLandArea=row['supplyLandArea']
        supplyLandNum=row['supplyLandNum']
        if supplyLandNum==0:
            list_supplyLandArea_div_supplyLandNum.append(0)
            continue
        supplyLandArea_div_supplyLandNum=float(supplyLandArea)/float(supplyLandNum)
        list_supplyLandArea_div_supplyLandNum.append(supplyLandArea_div_supplyLandNum)
    dict_supplyLandArea_div_supplyLandNum={'supplyLandArea_div_supplyLandNum':list_supplyLandArea_div_supplyLandNum}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_supplyLandArea_div_supplyLandNum)],axis=1)
    return df_ret

#本月成交套数+未成交套数=总套数
#总套数*新房成交均价

def add_totalNewNum(df_origin):
    df_ret=df_origin.copy()
    list_totalNewNum=[]
    for index,row in df_ret.iterrows():
        tradeNewNum=row['tradeNewNum']
        remainNewNum=row['remainNewNum']
        totalNewNum=float(tradeNewNum)+float(remainNewNum)
        list_totalNewNum.append(totalNewNum)
    dict_totalNewNum={'totalNewNum':list_totalNewNum}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_totalNewNum)],axis=1)
    return df_ret

def add_totalNewNum_mul_tradeNewMeanPrice(df_origin):
    df_ret=df_origin.copy()
    list_totalNewNum_mul_tradeNewMeanPrice=[]
    for index,row in df_ret.iterrows():
        tradeNewNum=row['tradeNewNum']
        remainNewNum=row['remainNewNum']
        tradeNewMeanPrice=row['tradeNewMeanPrice']
        totalNewNum=float(tradeNewNum)+float(remainNewNum)
        totalNewNum_mul_tradeNewMeanPrice=totalNewNum*float(tradeNewMeanPrice)
        list_totalNewNum_mul_tradeNewMeanPrice.append(totalNewNum_mul_tradeNewMeanPrice)
    dict_totalNewNum_mul_tradeNewMeanPrice={'totalNewNum_mul_tradeNewMeanPrice':list_totalNewNum_mul_tradeNewMeanPrice}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_totalNewNum_mul_tradeNewMeanPrice)],axis=1)
    return df_ret

#二手房成交总金额/二手房成交套数
#新房成交总金额/新房成交总套数

def add_totalTradeMoney_div_tradeSecNum(df_origin):
    df_ret=df_origin.copy()
    list_totalTradeMoney_div_tradeSecNum=[]
    for index,row in df_ret.iterrows():
        totalTradeMoney=row['totalTradeMoney']
        tradeSecNum=row['tradeSecNum']
        if tradeSecNum==0:
            list_totalTradeMoney_div_tradeSecNum.append(0)
            continue
        totalTradeMoney_div_tradeSecNum=float(totalTradeMoney)/float(tradeSecNum)
        list_totalTradeMoney_div_tradeSecNum.append(totalTradeMoney_div_tradeSecNum)
    dict_totalTradeMoney_div_tradeSecNum={'totalTradeMoney_div_tradeSecNum':list_totalTradeMoney_div_tradeSecNum}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_totalTradeMoney_div_tradeSecNum)],axis=1)
    return df_ret

def add_totalNewTradeMoney_div_tradeNewNum(df_origin):
    df_ret=df_origin.copy()
    list_totalNewTradeMoney_div_tradeNewNum=[]
    for index,row in df_ret.iterrows():
        totalNewTradeMoney=row['totalNewTradeMoney']
        tradeNewNum=row['tradeNewNum']
        if tradeNewNum==0:
            list_totalNewTradeMoney_div_tradeNewNum.append(0)
            continue
        totalNewTradeMoney_div_tradeNewNum=float(totalNewTradeMoney)/float(tradeNewNum)
        list_totalNewTradeMoney_div_tradeNewNum.append(totalNewTradeMoney_div_tradeNewNum)
    dict_totalNewTradeMoney_div_tradeNewNum={'totalNewTradeMoney_div_tradeNewNum':list_totalNewTradeMoney_div_tradeNewNum}
    df_ret=pd.concat([df_ret,pd.DataFrame(dict_totalNewTradeMoney_div_tradeNewNum)],axis=1)
    return df_ret

def add_none(df_origin):
    df_ret=df_origin
    return df_ret

def test_fun(df_processed,function):
    print(function.__name__," score= ",test_feature(df_processed, function))

def add_trademoney_div_area(df_processed,window_length=10):
    df_ret=df_processed.copy()
    dict_trademoney_div_area={}
    list_trademoney_div_area=[]
    left=0
    right=window_length
    while left<1050:
        df_tmp=df_ret[(df_ret['area']>=left)&(df_ret['area']<=right)]
        sum_area=df_tmp['area'].sum()
        sum_trademoney=df_tmp['tradeMoney'].sum()
        dict_trademoney_div_area[int(left/window_length)]=sum_trademoney/sum_area
        left+=window_length
        right+=window_length
    list_area=df_ret['area'].tolist()
    for area in list_area:
        list_trademoney_div_area.append(dict_trademoney_div_area[int(area/window_length)])
    df_ret=pd.concat([df_ret,pd.DataFrame({'trademoney_div_area':list_trademoney_div_area})],axis=1)
    return df_ret


def add_community_ave_trademoney_div_area(df_origin):
    df_ret = df_origin.copy()
    dict_commnityname_trademoney = {}
    for i in df_ret['communityName'].unique():
        df_tmp=df_ret[df_ret['communityName'] == i]
        trademoney_ave = df_tmp['tradeMoney'].sum()/df_tmp['area'].sum()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_ret.iterrows():
        communityname = row['communityName']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'community_ave_trademoney_div_area': list_trademoney_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret


def add_plate_ave_trademoney_div_area(df_origin):
    df_ret = df_origin.copy()
    dict_commnityname_trademoney = {}
    for i in df_ret['plate'].unique():
        df_tmp=df_ret[df_ret['plate'] == i]
        trademoney_ave = df_tmp['tradeMoney'].sum()/df_tmp['area'].sum()
        dict_commnityname_trademoney[i] = trademoney_ave
    list_trademoney_ave = []
    for index, row in df_ret.iterrows():
        communityname = row['plate']
        trademoney = dict_commnityname_trademoney[communityname]
        list_trademoney_ave.append(trademoney)
    dict_trademoney_final = {'plate_ave_trademoney_div_area': list_trademoney_ave}
    df_ret = pd.concat([df_ret, pd.DataFrame(dict_trademoney_final)], axis=1)
    return df_ret



df_processed = pd.read_csv(r"C:\Users\master\Desktop\future_lab\rental_predict\result\data_processed.csv")

df_processed['houseToward'] = df_processed['houseToward'].astype('category')
df_processed['rentType'] = df_processed['rentType'].astype('category')
df_processed['houseDecoration'] = df_processed['houseDecoration'].astype('category')
df_processed['houseFloor'] = df_processed['houseFloor'].astype('category')
df_processed['communityName'] = df_processed['communityName'].astype('category')
df_processed['region'] = df_processed['region'].astype('category')
df_processed['plate'] = df_processed['plate'].astype('category')

df_processed = df_processed.drop(columns=['tradeYear'])
df_processed = df_processed.drop(columns=['ID'])

df_processed=add_community_ave_trademoney(df_processed)
df_processed=add_region_ave_trademoney(df_processed)
df_processed=add_plate_ave_trademoney(df_processed)
df_processed=add_pv_div_uv(df_processed)
df_processed=add_month_ave_trademoney(df_processed)

list_function=[add_tradeyear_minus_buildyear,
               add_plate_num_in_region,
               add_community_num_in_plate,
               add_transport_total_num,
               add_education_total_num,
               add_service_total_num,
               add_lookNum_div_pv,
               add_lookNum_div_uv,
               add_totalWorkers_div_residentPopulation,
               add_newWorkers_div_totalWorkers,
               add_tradeLandArea_div_tradeLandNum,
               add_supplyLandArea_div_supplyLandNum,
               add_totalNewNum,
               add_totalNewNum_mul_tradeNewMeanPrice,
               add_totalTradeMoney_div_tradeSecNum,
               add_totalNewTradeMoney_div_tradeNewNum]
for function_name in list_function:
    test_fun(df_processed,function_name)

list_doubt_feature=['saleSecHouseNum',
                    'interSchoolNum',
                    'schoolNum',
                    'privateSchoolNum',
                    'hospitalNum',
                    'drugStoreNum',
                    'gymNum',
                    'bankNum',
                    'shopNum',
                    'parkNum',
                    'mallNum',
                    'superMarketNum',
                    'totalTradeMoney',
                    'totalTradeArea',
                    'tradeMeanPrice',
                    'tradeSecNum',
                    'totalNewTradeMoney',
                    'totalNewTradeArea',
                    'tradeNewMeanPrice',
                    'tradeNewNum',
                    'remainNewNum',
                    'supplyNewNum',
                    'supplyLandNum',
                    'tradeLandNum',
                    'tradeLandArea',
                    'landTotalPrice',
                    'landMeanPrice',
                    'residentPopulation',
                    'tradeMonth',
                    'tradeDay',
                    'bedroom',
                    'livingroom',
                    'bathroom']
for feature_name in list_doubt_feature:
    print("drop ",feature_name)
    test_fun(df_processed.drop(columns=[feature_name]),add_none)

test_fun(df_processed,add_trademoney_div_area)
test_fun(df_processed,add_plate_ave_trademoney_div_area)

for i in range(5,30):
    print("window_length=",i)
    test_fun(add_trademoney_div_area(df_processed,i),add_none)