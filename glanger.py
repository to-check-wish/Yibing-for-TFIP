#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import grangercausalitytests
import seaborn as sns


granger_1 = pd.read_csv("/Volumes/U_WHU_2T/eventrootcodecsv/granger_1.csv", parse_dates=['Date'], index_col='Date')
granger_2=granger_1.diff().dropna()

maxlag=30
test = 'ssr_chi2test'

def grangers_causation_matrix(data, variables, test='ssr_chi2test', verbose=False):  
    # From https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/
    """Check Granger Causality of all possible combinations of the Time series.
    The rows are the response variable, columns are predictors. The values in the table 
    are the P-Values. P-Values lesser than the significance level (0.05), implies 
    the Null Hypothesis that the coefficients of the corresponding past values is 
    zero, that is, the X does not cause Y can be rejected.

    data      : pandas dataframe containing the time series variables
    variables : list containing names of the time series variables.
    """
    df = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)
    for c in df.columns:
        for r in df.index:
            test_result = grangercausalitytests(data[[r, c]], maxlag=maxlag, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')
            min_p_value = np.min(p_values)
            df.loc[r, c] = min_p_value
    df.columns = [var + '_x' for var in variables]
    df.index = [var + '_y' for var in variables]
    return df


d = grangers_causation_matrix(granger_2, variables = granger_2.columns)

plt.subplots(figsize = (21,21))
sns.heatmap(d,annot = True,vmax = 1,square = True,cmap = "Reds")
plt.show()

#对不平稳对序列进行差分


#grangers_causation_matrix(series, variables = series.columns)
#series = amzn_transformed.loc[:, 'Close'].values
#amzn_transformed.plot(figsize=(14,8), legend=None, title='amzn_transformed Series');


# ADF Test
#result = adfuller(series, autolag='AIC')
#print(f'ADF Statistic: {result[0]}')
#print(f'n_lags: {result[1]}')
#print(f'p-value: {result[1]}')
#for key, value in result[4].items():
    #print('Critial Values:')
    #print(f'   {key}, {value}') 



