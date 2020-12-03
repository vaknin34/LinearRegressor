# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:36:11 2020

@author: vakni
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:32:08 2020

@author: vakni
"""
import DataPreProccessing
import LinearRegModel
import Visual
import pickle
class UI():
    def greetingUser(self):
        print('Hello User and Welcome to Csv Linear Regressor')
        
    def csvUpload(self):
        self.path = input("please enter Path to File")
        self.mainMenu()
        
    def DataPre(self):
        self.Data = DataPreProccessing.DataPreProcessing(self.path)
        self.Data.preprocess()
        self.mainMenu()
        
    def TrainModel(self):
        self.lrm = LinearRegModel.LinearRegModel()
        self.lrm.TrainModel(self.Data.x_train,self.Data.y_train)
        self.lrm.PredictTest(self.Data.x_test)
        self.mainMenu()
        
    def visualTrainng(self):
        self.vs = Visual.Visual(self.Data.x_train,self.Data.x_test,self.Data.y_train,self.Data.y_test,self.lrm.y_pred,self.lrm.regressor,self.Data.target_y,self.Data.feature_x)
        self.vs.VisualTrainngSet()
        self.mainMenu()
    
    def visualTest(self):
        self.vs.VisualTestSet()
        self.mainMenu()
    
    def saveModel(self):
        filename = 'Linear_Regressor_model.sav'
        pickle.dump(self.lrm.regressor, open(filename, 'wb'))
        self.mainMenu()
   
    def PredictSample(self):
       x = float(input("please enter one sample of " + self.Data.feature_x + " type"))
       print("prediction value is: " + str(self.lrm.regressor.predict([[x]])))
       self.mainMenu()
     
    def printLine(self):
        print(str(self.lrm.regressor.coef_) + " * x + " + str(self.lrm.regressor.intercept_))
        self.mainMenu()
       
   
    def mainMenu(self):
        print('choose 1 for csv upload')
        print('choose 2 for Data PreProcess')
        print('choose 3 for Training The Model')
        print('choose 4 for Visual Trainng Result')
        print('choose 5 for Visual Test Result')
        print('choose 6 to Save The Model')
        print('choose 7 to Predict One Sample')
        print('choose 8 to get Line Equation')
        print('choose 9 to exit')
        self.getUserInput()
    
    def getUserInput(self):
        x = int(input("plz choose Number "))
        while x < 1 or x > 9:
            print("Worng Number")
            x = int(input("plz choose Number "))
        if x == 1:
            self.csvUpload()
        if x == 2:
            self.DataPre()
        if x == 3:
            self.TrainModel()
        if x == 4:
            self.visualTrainng()
        if x == 5:
            self.visualTest()
        if x == 6:
            self.saveModel()
        if x == 7:
            self.PredictSample()
        if x == 8:
            self.printLine()
        if x == 9:
            print("Thank you for use my program see you next time")
   
            
            
            
            
        
            
            
            
            
            
            
