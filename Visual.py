# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:56:23 2020

@author: vakni
"""
import matplotlib.pyplot as plt


class Visual():
    def __init__(self,x_train,x_test,y_train,y_test,y_pred,regressor,target_name,feature_name):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        self.y_pred = y_pred
        self.regressor = regressor
        self.target_name = target_name
        self.feature_name = feature_name
        
    def VisualTrainngSet(self):
        plt.scatter(self.x_train,self.y_train,color='red')
        plt.plot(self.x_train,self.regressor.predict(self.x_train),color='blue')
        plt.title(self.target_name + " vs " +self.feature_name + " Traning set")
        plt.xlabel(self.feature_name)
        plt.ylabel(self.target_name)
        plt.show()
        
    def VisualTestSet(self):
        plt.scatter(self.x_test,self.y_test,color='red')
        plt.plot(self.x_train,self.regressor.predict(self.x_train),color='blue')
        plt.title(self.target_name + " vs " +self.feature_name + " Test set")
        plt.xlabel(self.feature_name)
        plt.ylabel(self.target_name)
        plt.show()
        
        
        
        