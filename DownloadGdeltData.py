# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime
import zipfile
import sys
import multiprocessing
import random
import os

# path = os.path.split(os.path.abspath(__file__))[0] + os.sep  
path = 'F:\\'
data_folder = path + 'gkg' + os.sep




def generate_url_list():
    url_idx='http://data.gdeltproject.org/gkg/'
    url_list=[]
    datestart = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
    dateend = datetime.datetime.strptime('2022-02-28', '%Y-%m-%d')
    date_list = []
    date_list.append(datestart.strftime('%Y-%m-%d').replace('-', ''))
    url_list.append(url_idx+datestart.strftime('%Y-%m-%d').replace('-', '')+'.gkg.csv.zip')
    while datestart < dateend:
        # 日期叠加一天
        datestart += datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y-%m-%d').replace('-', ''))
        url_list.append(url_idx + datestart.strftime('%Y-%m-%d').replace('-', '') + '.gkg.csv.zip')

    return url_list







def get_url_data(url):
    global data_folder
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)  
    filename = url.split('/')[-1]  
    filepath = data_folder + filename
    if os.path.exists(filepath) or os.path.exists(filepath[:-4]):  
        print('文件%s已存在' % filename)
        return
    print(filename)
    try:
        data = requests.get(url)
        with open(filepath, "wb") as f:
            f.write(data.content)
        fz = zipfile.ZipFile(filepath, 'r')
        fz.extract(fz.namelist()[0], data_folder) 
        fz.close()
        if os.path.exists(filepath):
            os.remove(filepath)  
    except Exception as e:
        print(e)
        log = open(path + 'log.txt', 'a')
        log.write(url + '\n')

def download():
    # url = 'http://data.gdeltproject.org/events/index.html'
    # print('获取文件链接', datetime.now())
    url_list = generate_url_list()
    # print('下载文件数据', datetime.now())
    pool = multiprocessing.Pool()  
    pool.map(get_url_data, url_list)

if __name__ == '__main__':
    url = 'http://data.gdeltproject.org/gkg/index.html'
    url_list=generate_url_list()
    print(url_list)
    download()
