# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:48:17 2014

@author: marvel
"""
import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ui_pingUI

class Ping(QDialog, ui_pingUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(Ping, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.pushButton.clicked.connect(self.callProgram)
        
        
    
    def dataReady(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll()))
        self.textEdit.ensureCursorVisible()

    def callProgram(self):
        # run the process
        # `start` takes the exec and a list of arguments
        cmd=self.lineEdit.text()              
        self.process.start('ping', [cmd])

    def initUI(self):
        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.pushButton.setEnabled(False))
        self.process.started.connect(lambda: self.lineEdit.setEnabled(False))        
        self.process.finished.connect(lambda: self.pushButton.setEnabled(True))
        self.process.finished.connect(lambda: self.lineEdit.setEnabled(True))
        #Stops the process        
        self.pushButton_2.clicked.connect(lambda: self.process.close())
        
def main():  
    app=QApplication(sys.argv)
    ping=Ping()
    ping.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()