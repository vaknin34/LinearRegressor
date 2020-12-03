# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:38:15 2020

@author: vakni
"""

from sklearn.linear_model import LinearRegression



class LinearRegModel():
    def __init__(self):
        self.regressor = LinearRegression()
    def TrainModel(self,x_train,y_train):
        self.regressor.fit(x_train,y_train)
        
    def PredictTest(self,x_test):
        self.y_pred =  self.regressor.predict(x_test)        
        
    
    

















