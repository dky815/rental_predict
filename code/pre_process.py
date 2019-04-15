import pandas as pd
import matplotlib.pyplot as plt
import re
import time

csv_file_train = pd.read_csv("../data/train_data.csv")
csv_file_test = pd.read_csv('../data/test_a.csv')


def rentType2number(rentstr):
    if rentstr == '未知方式' or rentstr == '--':
        return 0
    elif rentstr == '整租':
        return 1
    else:
        return 2


def houseFloor2number(floorstr):
    if floorstr == '低':
        return 0
    elif floorstr == '中':
        return 1
    else:
        return 2


def process_rentType(df_process):
    df_process['rentType'] = df_process['rentType'].map(rentType2number)
    return df_process


def process_houseType(df_process):
    list_bedroom = []
    list_livingroom = []
    list_bathroom = []
    for index, row in df_process.iterrows():
        house_str = row['houseType']
        list_num = re.findall('[0-9]+', house_str)
        list_bedroom.append(list_num[0])
        list_livingroom.append(list_num[1])
        list_bathroom.append(list_num[2])
    dict_room = {"bedroom": list_bedroom, "livingroom": list_livingroom, "bathroom": list_bathroom}
    df_room = pd.DataFrame(dict_room)
    df_res = pd.concat([df_process, df_room], axis=1)
    df_res.drop(['houseType'], axis=1, inplace=True)
    return df_res


def process_houseFloor(df_process):
    df_process['houseFloor'] = df_process['houseFloor'].map(houseFloor2number)
    return df_process


def proecss_houseToward(df_process):
    dict_toward = {
        'east': [],
        'south': [],
        'west': [],
        'north': [],
        'south_east': [],
        'south_west': [],
        'north_west': [],
        'north_east': [],
        'south_north': [],
        'east_west': [],
        'unknown': []
    }
    for index, row in df_process.iterrows():
        toward_str = row['houseToward']
        if toward_str == '东':
            for key, val in dict_toward.items():
                if key == 'east':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '南':
            for key, val in dict_toward.items():
                if key == 'south':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '西':
            for key, val in dict_toward.items():
                if key == 'west':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '北':
            for key, val in dict_toward.items():
                if key == 'north':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '东南':
            for key, val in dict_toward.items():
                if key == 'south_east':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '西南':
            for key, val in dict_toward.items():
                if key == 'south_west':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '西北':
            for key, val in dict_toward.items():
                if key == 'north_west':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '东北':
            for key, val in dict_toward.items():
                if key == 'north_east':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '南北':
            for key, val in dict_toward.items():
                if key == 'south_north':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        elif toward_str == '东西':
            for key, val in dict_toward.items():
                if key == 'east_west':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
        else:
            for key, val in dict_toward.items():
                if key == 'unknown':
                    dict_toward[key].append(1)
                else:
                    dict_toward[key].append(0)
    df_toward = pd.DataFrame(dict_toward)
    df_res = pd.concat([df_process, df_toward], axis=1)
    df_res.drop(['houseToward'], axis=1, inplace=True)
    return df_res


def process_houseDecoration(df_process):
    dict_decoration = {
        'other': [],
        'hardbound': [],
        'simple': [],
        'rough': []
    }
    for index, row in df_process.iterrows():
        decoration_str = row['houseDecoration']
        if decoration_str == '精装':
            for key, val in dict_decoration.items():
                if key == 'hardbound':
                    dict_decoration[key].append(1)
                else:
                    dict_decoration[key].append(0)
        elif decoration_str == '简装':
            for key, val in dict_decoration.items():
                if key == 'simple':
                    dict_decoration[key].append(1)
                else:
                    dict_decoration[key].append(0)
        elif decoration_str == '毛坯':
            for key, val in dict_decoration.items():
                if key == 'rough':
                    dict_decoration[key].append(1)
                else:
                    dict_decoration[key].append(0)
        else:
            for key, val in dict_decoration.items():
                if key == 'other':
                    dict_decoration[key].append(1)
                else:
                    dict_decoration[key].append(0)
    df_toward = pd.DataFrame(dict_decoration)
    df_res = pd.concat([df_process, df_toward], axis=1)
    df_res.drop(['houseDecoration'], axis=1, inplace=True)
    return df_res


def process_communityName(df_process):
    df_process['communityName'] = df_process['communityName'].map(lambda x: x[2:])
    return df_process


def process_city(df_process):
    df_process.drop(['city'], axis=1, inplace=True)
    return df_process


def process_tradeTime(df_process):
    list_year = []
    list_month = []
    list_day = []
    for index, row in df_process.iterrows():
        time_str = row['tradeTime']
        list_num = re.findall('[0-9]+', time_str)
        list_year.append(list_num[0])
        list_month.append(list_num[1])
        list_day.append(list_num[2])
    dict_time = {"year": list_year, "month": list_month, "day": list_day}
    df_time = pd.DataFrame(dict_time)
    df_res = pd.concat([df_process, df_time], axis=1)
    df_res.drop(['tradeTime'], axis=1, inplace=True)
    return df_res


def process_buildYear(df_process):
    df_process.loc[df_process['buildYear'] == '暂无信息', 'buildYear'] = 0
    df_process['buildYear'] = pd.to_numeric(df_process['buildYear'])
    total_value = df_process[df_process['buildYear'] != 0]['buildYear'].sum()
    total_num = (df_process['buildYear'] != 0).sum()
    ave = int(total_value / total_num)
    df_process.loc[df_process['buildYear'] == 0, 'buildYear'] = ave
    return df_process


def process_plate(df_process):
    df_process['plate'] = df_process['plate'].map(lambda x: x[2:])
    return df_process


def process_region(df_process):
    df_process['region'] = df_process['region'].map(lambda x: x[2:])
    return df_process


def preprocess(csv_file):
    df_new = csv_file.copy()
    df_new = process_rentType(df_new)
    df_new = process_houseType(df_new)
    df_new = process_houseFloor(df_new)
    df_new = proecss_houseToward(df_new)
    df_new = process_houseDecoration(df_new)
    df_new = process_communityName(df_new)
    df_new = process_city(df_new)
    df_new = process_tradeTime(df_new)
    df_new = process_buildYear(df_new)
    df_new = process_plate(df_new)
    df_new = process_region(df_new)
    return df_new


if __name__ == "__main__":
    start_time = time.time()
    df_new = preprocess(csv_file_train)
    df_new.to_csv('../result/data_processed.csv')
    end_time = time.time()
    print("cost time = " + str(end_time - start_time))
