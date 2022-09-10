#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Importing dependencies
import numpy as np
np.random.seed(1)
import tensorflow
tensorflow.random.set_seed(2)
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
from keras.layers.core import Dense
from keras.layers.recurrent import GRU
from keras import optimizers
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import datetime as dt
import time

plt.style.use('ggplot')
# Setting up an early stop
earlystop = EarlyStopping(monitor='loss', min_delta=0.0001, patience=80,  verbose=1, mode='min')
callbacks_list = [earlystop]
df = pd.read_csv("/Volumes/U_WHU_2T/dvn_final.csv", parse_dates=['Date'], index_col='Date')
train = df[:436]
test = df[436:]
sc = MinMaxScaler()
train = sc.fit_transform(train)
sc = MinMaxScaler()
test = sc.fit_transform(test)
print(train.shape,test.shape)

#Build and train the model
def fit_model(train, lookback, hl, lr, batch, epochs):
    # Function from https://github.com/ninja3697/Stocks-Price-Prediction-using-Multivariate-Analysis/blob/master/Multivatiate-GRU/Multivariate-3-GRU.ipynb
    '''
    Fitting the GRU model by reshaping the input training and validate data into the
    right dimension. Compose the layers for the Deep Learning Model and fitting the model.
    
    INPUT:
        train - (np.array) Input Traning Data for fitting the model
        val - (np.array) Input Validate Data for model feedback
        lookback - (int) number of timesteps to look back to predict the current one
        hl - (list of int) of different output dimensions for GRU layers
        lr - (float) learning rate for Adam optimizer
        batch - (int) Number of data points per full layer calculation
        epochs - (int) Number of full Training Iterations
    OUTPUT:
        model - (keras GRU model) includes the fitted GRU model
        history['loss'] - (np.array) Train Loss Values over Epochs
        history['val_loss'] - (np.array) Validate Loss Values over Epochs
    '''
    X_train = []
    Y_train = []
    X_val = []
    Y_val = []
    # Prepare Train Data from Pandas Series to Numpy compliant Matrix 
    # and split Input DataFrame into Features and Result Vector
    for i in range(lookback,train.shape[0]):
        X_train.append(train[i-lookback:i])
        Y_train.append(train[i][0])
    X_train,Y_train = np.array(X_train),np.array(Y_train)

  
    # Adding Layers to the model
    model = Sequential()
    # composing the GRU layers, honestly doesn't fully understand the advantages of this explicit architecture therefore I've to do a lot more Deep Learning research
    model.add(GRU(X_train.shape[2],input_shape = (X_train.shape[1],X_train.shape[2]),return_sequences = True,
                  activation = 'relu'))
    for i in range(len(hl)-1):        
        model.add(GRU(hl[i],activation = 'relu',return_sequences = True))
    model.add(GRU(hl[-1],activation = 'relu'))
    # matrix multiplication that will apply the new weights to the trainable parameters
    model.add(Dense(1))
    # Adam is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments
    model.compile(optimizer = optimizers.adam_v2.Adam(lr = lr), loss = 'mean_squared_error')
  
    # Training the data
    history = model.fit(X_train,Y_train,epochs = epochs,batch_size = batch,verbose = 0,
                        shuffle = False, callbacks=callbacks_list)
    model.reset_states()
    return model, history.history['loss']

# Evaluating the model
def evaluate_model(model,test,lookback):
    # Function from https://github.com/ninja3697/Stocks-Price-Prediction-using-Multivariate-Analysis/blob/master/Multivatiate-GRU/Multivariate-3-GRU.ipynb
    '''
    Predicts the test data against the fitted GRU model and calculates
    multiple error values for evaluation.
    
    INPUT:
        model - (keras GRU model)
        test - (DataFrame) with the time series test split
        lookback - (int) Timesteps to look into the past
    OUTPUT:
        mse - (float) mean-squared-error between true and prediction chart
        rmse - (float) root-mean-squared-error between true and prediction chart
        r2 - (float) r2 error between true and prediction chart
        Y_test - (np.array) scaled true chart
        Y_hat - (np.array) scaled prediction chart
    '''
    
    X_test = []
    Y_test = []

    # Prepare Test Data from Pandas Series to Numpy compliant Matrix 
    # and split Input DataFrame into Features and Result Vector
    for i in range(lookback,test.shape[0]):
        X_test.append(test[i-lookback:i])
        Y_test.append(test[i][0])
    X_test,Y_test = np.array(X_test),np.array(Y_test)
  

    Y_hat = model.predict(X_test)
    mse = mean_squared_error(Y_test,Y_hat)
    rmse = sqrt(mse)
    r2 = r2_score(Y_test,Y_hat)
    return mse, rmse, r2, Y_test, Y_hat
  
    # Plotting the predictions
def plot_data(Y_test,Y_hat, ax="", title=""):
    '''
    Plots the test-data against the prediction-data
    '''
    if ax:
        plot = ax
    else:
        fig, ax = plt.subplots(1, 1)
        plot = ax

    plot.plot(Y_test,c = 'r')
    plot.plot(Y_hat,c = 'y')
    plot.set_xlabel('Day')
    plot.set_ylabel('Price')
    if not title:
        plot.set_title("esi Prediction using Multivariate-GRU")
    else:
        plot.set_title(title)
    plot.legend(['Actual','Predicted'],loc = 'lower right')
    #plot.show()

# Plotting the training errors
def plot_error(train_loss,ax="", title=""):
    '''
    Plots the train loss of error against the validation loss of error.
    '''
    if ax:
        plot = ax
    else:
        fig, ax = plt.subplots(1, 1)
        plot = ax
        
    plot.plot(train_loss,c = 'r')
    plot.set_ylabel('Loss')
    plot.set_xlabel('Epochs')
    if not title:
        plot.set_title('Loss Plot for esi')
    else:
        plot.set_title(title)
    plot.legend(['train'],loc = 'lower right')
    #plot.show()
    
# Lookback describes how many data points we will look into the past to describe the current data point
lookback = 5
# dimensions of the output of the layer
hl = [40,35]
# learning rate for adam algorithm optimization https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam
lr = 1e-4
# number of data points in the training set to update network weights in one iteration
batch_size = 64
# number of complete iterations over my input dataset, one iteration consists of len(train)/batch_size batches
num_epochs = 200

model,train_error = fit_model(train,
                                        lookback,
                                        hl,
                                        lr,
                                        batch_size,
                                        num_epochs)
plot_error(train_error)

mse,rmse,r2_value,true,predicted = evaluate_model(model, test, 5)
print("MSE =",mse)
print("RMSE =",rmse)
print("R2-Score =",r2_value)
plot_data(true,predicted)
  
