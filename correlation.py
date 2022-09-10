#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
