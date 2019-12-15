'''
Created on 15.12.2019

@author: Juho
'''
#import serial

class TOIMINTA():
    
    def __init__(self):
        
        #??
        self.kupit = 1
    
    def get_self(self):
        
        return self   
        
    def get_kupit(self):
        
        return self.kupit
    def set_kupit(self,amount):
        
        self.kupit = amount
        print(self.get_kupit())
        