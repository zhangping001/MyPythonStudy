# -*- coding: utf-8 -*-

'''
    【简介】
	 QSS样式
    
'''

from PyQt5.QtWidgets import *
import sys  
    
class WindowDemo(QWidget):  
	def __init__(self ):  
		super().__init__()
		
			
		btn2 = QPushButton(self )  
		btn2.setText('按钮2')
		
		btn1 = QPushButton(self )  
		btn1.setText('按钮1')
	
		
		vbox=QVBoxLayout()
		vbox.addWidget(btn2)
		vbox.addWidget(btn1)
			  
		self.setLayout(vbox)
		self.setWindowTitle("QSS样式")
  
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	win = WindowDemo()  
	qssStyle = '''      			  			
			QPushButton { 
				background-color: red 
			}
				
		'''
	win.setStyleSheet( qssStyle ) 				
	win.show()  
	sys.exit(app.exec_())

