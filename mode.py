#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:11:34 2022

@author: kelly
"""

DJI_transformed = DJI.diff().dropna()
GSPC_transformed = GSPC.diff().dropna()
IXIC_transformed = IXIC.diff().dropna()
ms_transformed = ms.diff().dropna()
pfe_transformed = pfe.diff().dropna()
dvn_transformed = dvn.diff().dropna()
amzn_transformed = amzn.diff().dropna()
eventrootcode_1_transformed = eventrootcode_1.diff().dropna()
eventrootcode_2_transformed = eventrootcode_2.diff().dropna()
eventrootcode_7_transformed = eventrootcode_7.diff().dropna()
eventrootcode_8_transformed = eventrootcode_8.diff().dropna()
eventrootcode_10_transformed = eventrootcode_10.diff().dropna()
eventrootcode_13_transformed = eventrootcode_13.diff().dropna()
eventrootcode_13_transformed.to_csv("/Volumes/U_WHU_2T/eventrootcodecsv/13_transformed.csv", index=True, header=True)

eventrootcode_1 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/1.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_2 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/2.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_3 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/3.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_4 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/4.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_5 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/5.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_6 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/6.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_7 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/7.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_8 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/8.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_9 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/9.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_10 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/10.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_11 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/11.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_12 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/12.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_13 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/13.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_14 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/14.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_15 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/15.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_16 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/16.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_17 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/17.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_18 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/18.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_19 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/19.csv", parse_dates=['Date'], index_col='Date')
eventrootcode_20 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/20.csv", parse_dates=['Date'], index_col='Date')


DJI = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^DJI.csv", parse_dates=['Date'], index_col='Date')
GSPC = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^GSPC.csv", parse_dates=['Date'], index_col='Date')
IXIC = pd.read_csv("/Volumes/U_WHU_2T/indextotal/index/^IXIC.csv", parse_dates=['Date'], index_col='Date')
ual = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Airlines/ual.csv", parse_dates=['Date'], index_col='Date')
ms = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Banking/ms.csv", parse_dates=['Date'], index_col='Date')
pfe = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Healthcare/pfe.csv", parse_dates=['Date'], index_col='Date')
dvn = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Oil & Energy/dvn.csv", parse_dates=['Date'], index_col='Date')
amzn = pd.read_csv("/Volumes/U_WHU_2T/indextotal/Technology/amzn.csv", parse_dates=['Date'], index_col='Date')
