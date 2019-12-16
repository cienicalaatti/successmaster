'''
Created on 15.12.2019

@author: Juho
'''
from toiminta import TOIMINTA
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QStackedLayout, QStackedWidget,QFont
from PyQt5.Qt import QGraphicsRectItem, QColor, QBrush, QRect, QSize, QIcon,\
    QPoint, QHoverEvent, QMouseEvent, QCursor, QWidget, QLabel, QPixmap, QFont,\
    QGraphicsTextItem, QPushButton

class GRAFIIKKA(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.stack = QtWidgets.QStackedWidget()
        
        self.setCentralWidget(self.stack)
        
        self.hlayout = QtWidgets.QHBoxLayout()
        
        self.centralWidget().setLayout(self.hlayout)
        
        self.toiminta = TOIMINTA()
        
        self.valinta = VALINTA(self.get_self())
        
        self.keitto = KEITTO(self.get_self())
        
        self.stack.addWidget(self.valinta)
        self.stack.addWidget(self.keitto)
        
        self.init_window()
        
    
    def get_self(self):
        
        return self
        
        
        
    def init_window(self):
     
     
        self.setGeometry(200, 100, 800, 800)
        self.setWindowTitle('kahvisovellus')
        self.show()
    
    def switch(self):
        
        if self.stack.currentIndex() == 0:
            self.stack.setCurrentIndex(1)
        else:
            self.stack.setCurrentIndex(0)


class VALINTA(QtWidgets.QWidget):
    
    def __init__(self,stack):
        super().__init__()
        self.horizontal = QtWidgets.QHBoxLayout()
        self.vertical = QtWidgets.QVBoxLayout()
        self.setLayout(self.horizontal)
        self.horizontal.addLayout(self.vertical)
        
        self.stack = stack
        
        self.add_widgets()
    
    def add_widgets(self):
        
        self.logo = QtWidgets.QLabel(self)
        self.logo.setPixmap(QPixmap("logo.png"))
        self.logo.setMinimumSize(200,100)
        self.logo.setMaximumSize(200, 100)
        self.vertical.addWidget(self.logo)
        
        self.increment = QtWidgets.QSpinBox()
        self.increment.setMinimum(1)
        self.increment.setMaximum(10)
        self.increment.setValue(1)
        self.vertical.addWidget(self.increment)
        
        self.button = QtWidgets.QPushButton("Start")
        self.button.setMinimumSize(100, 100)
        self.button.setMaximumSize(120, 120)
        self.button.clicked.connect(self.switch)
        #self.button.clicked.connect(self.stack.toiminta.set_kupit(self.increment.value()))
        
        self.vertical.addWidget(self.button)
        
    def switch(self):
        
        self.stack.toiminta.set_amount(self.increment.value())
        
        self.stack.switch()
        
        
        

class KEITTO(QtWidgets.QWidget):
    
    def __init__(self,stack):
        super().__init__()
        self.horizontal = QtWidgets.QHBoxLayout()
        self.vertical = QtWidgets.QVBoxLayout()
        self.setLayout(self.horizontal)
        self.horizontal.addLayout(self.vertical)
        
        self.stack = stack
        
        self.add_widgets()
        
    def add_widgets(self):
        
        self.label = QtWidgets.QLabel("Kahvit on tippumassa!")
        self.label.setFont(QFont("Arial Rounded MT Bold",30))
        self.vertical.addWidget(self.label)
        
        
        self.finish_button = QtWidgets.QPushButton("Valmista")
        self.finish_button.setMinimumSize(100, 100)
        self.finish_button.setMaximumSize(120, 120)
        self.finish_button.clicked.connect(self.switch)
        self.vertical.addWidget(self.finish_button)
        
    def switch(self):
        
        self.stack.toiminta.stop()
        self.stack.switch()
        
        
        
        
        
        
