'''
Created on 15.12.2019

@author: Juho
'''
import serial,time
from time import sleep

class TOIMINTA():
    
    def __init__(self):
        
        #??
        self.kupit = 1
        
        self.start_serial()
        
        self.keitto = False
        
    def get_self(self):
        
        return self   
        
    def get_kupit(self):
        
        return self.kupit
    def set_amount(self,amount):
        
        self.kupit = amount
        
        self.keitto = True
        
        n = str(self.get_kupit())
        
        self.arduino.write(n.encode())
        
        
    def stop(self):
        self.arduino.write(b'n')
        
        self.keitto = False
        

    
    def start_serial(self):
        self.arduino = serial.Serial('COM4', 9600, timeout=.1)
        
    