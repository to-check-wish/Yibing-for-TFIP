#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:30:53 2022

@author: kelly
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import numpy as np
import pandas as pd

eventrootcode_1 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/1.csv")
eventrootcode_2 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/2.csv")
eventrootcode_3 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/3.csv")
eventrootcode_4 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/4.csv")
eventrootcode_5 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/5.csv")
eventrootcode_6 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/6.csv")
eventrootcode_7 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/7.csv")
eventrootcode_8 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/8.csv")
eventrootcode_9 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/9.csv")
eventrootcode_10 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/10.csv")
eventrootcode_11 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/11.csv")
eventrootcode_12 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/12.csv")
eventrootcode_13 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/13.csv")
eventrootcode_14 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/14.csv")
eventrootcode_15 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/15.csv")
eventrootcode_16 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/16.csv")
eventrootcode_17 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/17.csv")
eventrootcode_18 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/18.csv")
eventrootcode_19 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/19.csv")
eventrootcode_20 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/20.csv")


DJI = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^DJI.csv")
GSPC = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^GSPC.csv")
IXIC = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^IXIC.csv")

aal = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Airlines/aal.csv")
luv = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Airlines/luv.csv")
ual = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Airlines/ual.csv")

gs = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Banking/gs.csv")
jpm = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Banking/jpm.csv")
ms = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Banking/ms.csv")

abbv = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Healthcare/abbv.csv")
gild = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Healthcare/gild.csv")
pfe = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Healthcare/pfe.csv")

cvx = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Oil & Energy/cvx.csv")
dvn = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Oil & Energy/dvn.csv")
xom = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Oil & Energy/xom.csv")

aapl = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Technology/aapl.csv")
amzn = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Technology/amzn.csv")
msft = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Technology/msft.csv")

def convert_values(row, col):
    '''
    Function for pandas per-row apply function. Converts value from specified "col" from
    "5,343.504" to float representation.
    
    INPUT:
        row - (Row of DataFrame) Row with at least one string representation of float value
        col - (str) Name of column with the string representation of float value
    
    OUTPUT:
        val - (float) Returns float value
    '''
    try:
        val = row[col].replace(",","")
    except:
        val = row[col]
    return float(val)

def prep_charts(df):
    '''
    Function to execute apply function on different float values in stock market data.
    Set Date as Index and Order by index. 
    
    INPUT:
        df - (DataFrame) with at least Columns "Price", "Open", "High", "Low" and "Date"
    
    OUTPUT:
        df - (DataFrame) with datetime index and all string values converted to float
    '''
    df["Close"] = df.apply(convert_values, args=("Close",), axis=1)
    df["Open"] = df.apply(convert_values, args=("Open",), axis=1)
    df["High"] = df.apply(convert_values, args=("High",), axis=1)
    df["Low"] = df.apply(convert_values, args=("Low",), axis=1)
    df["NumMentions"] = df.apply(convert_values, args=("NumMentions",), axis=1)
    df["AvgTone"] = df.apply(convert_values, args=("AvgTone",), axis=1)
    df["GoldsteinScale"] = df.apply(convert_values, args=("GoldsteinScale",), axis=1)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date").reset_index()
    del df["index"]   
    df["Close_norm"] = df["Close"] / df["Close"].max()
    return df

eventrootcode_1 = prep_charts(eventrootcode_1)
eventrootcode_2 = prep_charts(eventrootcode_2)
eventrootcode_3 = prep_charts(eventrootcode_3)
eventrootcode_4 = prep_charts(eventrootcode_4)
eventrootcode_5 = prep_charts(eventrootcode_5)
eventrootcode_6 = prep_charts(eventrootcode_6)
eventrootcode_7 = prep_charts(eventrootcode_7)
eventrootcode_8 = prep_charts(eventrootcode_8)
eventrootcode_9 = prep_charts(eventrootcode_9)
eventrootcode_10 = prep_charts(eventrootcode_10)
eventrootcode_11 = prep_charts(eventrootcode_11)
eventrootcode_12 = prep_charts(eventrootcode_12)
eventrootcode_13 = prep_charts(eventrootcode_13)
eventrootcode_14 = prep_charts(eventrootcode_14)
eventrootcode_15 = prep_charts(eventrootcode_15)
eventrootcode_16 = prep_charts(eventrootcode_16)
eventrootcode_17 = prep_charts(eventrootcode_17)
eventrootcode_18 = prep_charts(eventrootcode_18)
eventrootcode_19 = prep_charts(eventrootcode_19)
eventrootcode_20 = prep_charts(eventrootcode_20)


DJI = prep_charts(DJI)
GSPC = prep_charts(GSPC)
IXIC = prep_charts(IXIC)

aal = prep_charts(aal)
luv = prep_charts(luv)
ual = prep_charts(ual)

gs = prep_charts(gs)
jpm = prep_charts(jpm)
ms = prep_charts(ms)

abbv = prep_charts(abbv)
gild = prep_charts(gild)
pfe = prep_charts(pfe)

cvx = prep_charts(cvx)
dvn = prep_charts(dvn)
xom = prep_charts(xom)

aapl = prep_charts(aapl)
amzn = prep_charts(amzn)
msft = prep_charts(msft)

DJI["30_day_ma"] = DJI["Close"].rolling(window=30, min_periods=1).mean()
DJI["30_day_std"] = DJI["Close"].rolling(window=30, min_periods=1).std()
DJI["boll_upp"] = DJI['30_day_ma'] + (DJI['30_day_std'] * 2)
DJI["boll_low"] = DJI['30_day_ma'] - (DJI['30_day_std'] * 2)
                 
#Merge the seperate datasets into one DataFrame:
corr_df = DJI[["Date","Close", "High", "Low", "30_day_ma", "30_day_std", "boll_upp", "boll_low"]]
corr_df.columns = ["DJI_{}".format(x) for x in corr_df.columns]
corr_df.loc[:,"1_AvgTone"] = eventrootcode_1["AvgTone"]
corr_df.loc[:,"2_AvgTone"] = eventrootcode_2["AvgTone"]
corr_df.loc[:,"3_AvgTone"] = eventrootcode_3["AvgTone"]
corr_df.loc[:,"4_AvgTone"] = eventrootcode_4["AvgTone"]
corr_df.loc[:,"5_AvgTone"] = eventrootcode_5["AvgTone"]
corr_df.loc[:,"6_AvgTone"] = eventrootcode_6["AvgTone"]
corr_df.loc[:,"7_AvgTone"] = eventrootcode_7["AvgTone"]
corr_df.loc[:,"8_AvgTone"] = eventrootcode_8["AvgTone"]
corr_df.loc[:,"9_AvgTone"] = eventrootcode_9["AvgTone"]
corr_df.loc[:,"10_AvgTone"] = eventrootcode_10["AvgTone"]
corr_df.loc[:,"11_AvgTone"] = eventrootcode_11["AvgTone"]
corr_df.loc[:,"12_AvgTone"] = eventrootcode_12["AvgTone"]
corr_df.loc[:,"13_AvgTone"] = eventrootcode_13["AvgTone"]
corr_df.loc[:,"14_AvgTone"] = eventrootcode_14["AvgTone"]
corr_df.loc[:,"15_AvgTone"] = eventrootcode_15["AvgTone"]
corr_df.loc[:,"16_AvgTone"] = eventrootcode_16["AvgTone"]
corr_df.loc[:,"17_AvgTone"] = eventrootcode_17["AvgTone"]
corr_df.loc[:,"18_AvgTone"] = eventrootcode_18["AvgTone"]
corr_df.loc[:,"19_AvgTone"] = eventrootcode_19["AvgTone"]
corr_df.loc[:,"20_AvgTone"] = eventrootcode_20["AvgTone"]

corr = corr_df.corr()
coordinates = corr.values.tolist()
columns = list(corr.columns)

trace1 = {
        "type": "heatmap", 
        "x": columns, 
        "y": columns, 
        "z": coordinates,
        "colorscale": 'viridis'
        }
    
data = trace1
layout = {"title": "Correlation Between DJI Chart Indicators",
          "width": 1200,
          "height": 1000}
fig = go.Figure(dict(data=data, layout=layout))
fig.show()