# -*- coding: utf-8 -*-
"""
Created on 2022/2/28 16:03
@author : zsj

"""

import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import json
import requests
import datetime
import yfinance as yf

with open("D:\\OneDrive\\Documents\\a研究生毕业论文\\code\\results\\stock_industry_update.json", 'r',
          encoding='utf-8') as f:
    stock_list = json.load(f)


def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    print(tickers)

    return tickers

def LoadStockData(stock_name):
    start = datetime.datetime(2022, 1, 1)
    end = datetime.datetime(2022, 2, 1)
    stock_data = yf.Ticker(stock_name)
    stock_data_historical = stock_data.history(start="2018-01-01", end="2022-03-10", interval="1d")
    stock_data_historical.to_csv('E:\\毕业论文_研\\数据\\stock_data_18-today\\'+stock_name+'.csv')
    print('Already download {}'.format(stock_name))

if __name__ == '__main__':
    stock_list['index']=['^DJI','^GSPC','^IXIC']

    for i in stock_list:
        print(i)
        for j in stock_list[i]:
            if not os.path.exists('E:\\毕业论文_研\\数据\\stock_data_18-today\\'+j+'.csv'):
                LoadStockData(j)
            else:
                print('Already have {}'.format(j))