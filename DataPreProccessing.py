# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:14:55 2020

@author: vakni
"""

import pandas as pd
from sklearn.model_selection import train_test_split


class DataPreProcessing():
    
    def __init__(self,csvfilename):
        self.df = pd.read_csv(csvfilename)
    
    def preprocess(self):
        col_list = list(self.df.columns)
        for i in range(len(col_list)):
            print(str(i) + " : " + col_list[i])
        self.feature_x = int(input("please choose feature x column number"))
        self.feature_x = col_list[self.feature_x]
        x = self.df[self.feature_x].values
        self.target_y = int(input("please choose target y column number"))
        self.target_y = col_list[self.target_y]
        y = self.df[self.target_y].values
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
        self.x_train = x_train.reshape(-1, 1)
        self.x_test = x_test.reshape(-1, 1)
        self.y_train = y_train.reshape(-1, 1)
        self.y_test = y_test.reshape(-1, 1)
        




















