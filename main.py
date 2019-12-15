'''
Created on 15.12.2019

@author: Juho
'''
import sys
from PyQt5.QtWidgets import QApplication
#from GUI import GUI
from GUI import GRAFIIKKA,VALINTA,KEITTO
from Tools.scripts.serve import app


def main():       
    
    global app
    app = QApplication(sys.argv)
    menu = GRAFIIKKA()
    sys.exit(app.exec_())
    
main()
