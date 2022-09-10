# -*- coding: utf-8 -*-
import datetime
import os

import numpy as np
import json
import pandas as pd

col_names = ['GLOBALEVENTID', 'SQLDATE', 'MonthYear', 'Year', 'FractionDate', 'Actor1Code', 'Actor1Name',
             'Actor1CountryCode', 'Actor1KnownGroupCode', 'Actor1EthnicCode', 'Actor1Religion1Code',
             'Actor1Religion2Code', 'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', 'Actor2Code',
             'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode', 'Actor2EthnicCode', 'Actor2Religion1Code',
             'Actor2Religion2Code', 'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', 'IsRootEvent',
             'EventCode', 'EventBaseCode', 'EventRootCode', 'QuadClass', 'GoldsteinScale', 'NumMentions',
             'NumSources', 'NumArticles', 'AvgTone', 'Actor1Geo_Type', 'Actor1Geo_FullName',
             'Actor1Geo_CountryCode', 'Actor1Geo_ADM1Code', 'Actor1Geo_Lat', 'Actor1Geo_Long',
             'Actor1Geo_FeatureID', 'Actor2Geo_Type', 'Actor2Geo_FullName', 'Actor2Geo_CountryCode',
             'Actor2Geo_ADM1Code', 'Actor2Geo_Lat', 'Actor2Geo_Long', 'Actor2Geo_FeatureID', 'ActionGeo_Type',
             'ActionGeo_FullName', 'ActionGeo_CountryCode', 'ActionGeo_ADM1Code', 'ActionGeo_Lat',
             'ActionGeo_Long', 'ActionGeo_FeatureID', 'DATEADDED', 'SOURCEURL']


def create_assist_date(datestart, dateend):
    # 创建日期辅助表函数

    if datestart is None:
        datestart = '2020-01-01'
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y-%m-%d')

    # 转为日期格式
    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    date_list = []
    date_list.append(datestart.strftime('%Y-%m-%d').replace('-', ''))
    while datestart < dateend:
        # 日期叠加一天
        datestart += datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y-%m-%d').replace('-', ''))

    return date_list


def cal_mutiList_sum(list):
    #计算列表的总和
    l = np.array(list)
    res = l.sum(axis=0)
    print(res.tolist())
    return res.tolist()


def event_data(date, root_path="/Volumes/U_WHU_2T/gdelt/"):
    #
    path = root_path + date + '.export.CSV'
    data = pd.read_csv(path, sep='\t', encoding="utf-8", engine='python')

    print(len(data))
    data.columns = col_names
    # root_code = data['EventRootCode'].values.tolist()
    root_code = [i for i in range(1, 21)]

    event_list = {c: [] for c in root_code}
    for i in range(len(data)):
        # print(data.loc[i, 'EventRootCode'],data.loc[i, 'NumMentions'], data.loc[i, 'AvgTone'],data.loc[i, 'GoldsteinScale'])
        try:
            event_root_code = int(data.loc[i, 'EventRootCode'])
            nm = data.loc[i, 'NumMentions']
            avg_tone = data.loc[i, 'AvgTone']
            gs = data.loc[i, 'GoldsteinScale']
            event_list[event_root_code].append([nm, avg_tone, gs])
        except:
            print(data.loc[i, 'EventRootCode'])


        # print(type(num_mentions),type(avg_tone),type(goldstein))
    event_data_day = {}
    for i in range(1, 21):
        event_data_day[i] = cal_mutiList_sum(event_list[i])
    return event_data_day


def get_event_code_data(date, root_path="/Volumes/U_WHU_2T/gdelt/"):
    path = root_path + date + '.export.CSV'
    data = pd.read_csv(path, sep='\t', encoding="utf-8", engine='python')
    data.columns = col_names
    print(data['EventCode'])

    event_list={}
    for i in range(len(data)):
        try:
            event_code = int(data.loc[i, 'EventCode'])
            nm = data.loc[i, 'NumMentions']
            avg_tone = data.loc[i, 'AvgTone']
            gs = data.loc[i, 'GoldsteinScale']
            if event_code not in event_list:
                event_list[event_code]=[]
                event_list[event_code].append([nm, avg_tone, gs])
            else:
                event_list[event_code].append([nm, avg_tone, gs])
        except:
            print("error")

    event_data_day = {}
    for i in event_list:
        event_data_day[i] = cal_mutiList_sum(event_list[i])
    print(len(event_data_day))

    return event_data_day


def generate_event_code_series_data():
    # 生成日期列表
    date_list = create_assist_date('2020-01-01', '2022-02-28')
    event_data_list={}
    for day in  date_list:
        if os.path.exists("/Volumes/U_WHU_2T/gdelt/"+ day + '.export.CSV'):
            print(day)
            event_data_list[day]=get_event_code_data(day)
        else:
            print(day, 'is not exsit')
    print(event_data_list)


def main():
    #生成日期列表
    date_list=create_assist_date('2020-01-01', '2022-02-28')
    root_code = [i for i in range(1, 21)]
    event_list = {c: {} for c in root_code}
    #按照eventCode分别存放sumOftone and sumOfgs
    for day in date_list:

        if os.path.exists("/Volumes/U_WHU_2T/gdelt/"+ day + '.export.CSV'):
            print(day)
            event_data_day=event_data(day)
            for i in range(1,21):
                event_list[i][day]=event_data_day[i]
        else:
            print(day,'is not exsit')

    print(event_list)
    for key in event_list:
        with open("/Volumes/U_WHU_2T/event/"+str(key)+".csv", 'w', encoding="utf-8") as f:
            json.dump(event_list[key], f)
        print('RootCode '+str(key)+' finish')


if __name__ == '__main__':
    main()

    # generate_event_code_series_data()
