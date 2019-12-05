'''
Created on 5.12.2019

@author: Juho
'''
import serial,time

arduino = serial.Serial('COM3', 9600, timeout=.1)

time.sleep(1)

