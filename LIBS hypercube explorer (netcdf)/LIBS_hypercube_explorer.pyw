# -*- coding: utf-8 -*-
"""
10 11 23 _ v1

@author: Christian
"""


appname = "LIBS Hypercube explorer v1.0"

import sys, time

from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.uic import loadUiType

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

import matplotlib.pyplot as plt
import pandas as pd
import os

import numpy as np
import xarray as xr

from collections import OrderedDict
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

cmaps = OrderedDict()


fileName="0"
value=300

cmaps['Sequential'] = ['viridis', 'viridis_r', 'plasma',
                       'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds']


# Image widget
class ImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        self.setMinimumSize(image.size())
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0, 0), self.image)
        qp.end()


# Main window-----------------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow):

    text_update = QtCore.pyqtSignal(str)    

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)

    # Create main window

        uic.loadUi('Slider_hypercube.ui', self)

        
        self.actionOpen_hypercube.triggered.connect(self.open_cube_Dialog)
        self.baseline_wavelength.valueChanged['int'].connect(lambda: self.change_graph(fileName))
        self.horizontalSlider.valueChanged['int'].connect(lambda: self.change_graph(fileName))
        self.colormap_comboBox.addItems(cmaps['Sequential'])

        self.colormap_comboBox.setCurrentIndex(0)          
        self.colormap_comboBox.currentIndexChanged.connect(lambda: self.change_graph(fileName)) 
        self.transpose_checkBox.stateChanged.connect(lambda: self.change_graph(fileName))


        self.trace_graph(fileName)
        

        
        self.text_update.connect(self.append_text)
        sys.stdout = self

# ----------------------------------------------------------------------------

           
    # Start image capture & display


 
    def change_graph(self,fileName):
        self.rmmpl()

        self.trace_graph(fileName)



    def trace_graph(self,fileName):
        

        fig1 = Figure()

        if fileName != "0":          
           
            fig1.set_tight_layout(True) #use all the space in the tab

            ax1 = fig1.add_subplot()  #add just one graph


            global libs_cube
            libs_cube = xr.open_dataarray(fileName)
            libs_cube = libs_cube.sortby('bands')
            #Now, it's possible to make a selection a particulr wavelength,
            #using the "nearest" method of xarray selection
            
            #test = libs_cube.sel(bands=(self.hypercube_wavelength.value()/10), method="nearest")
            test=libs_cube[self.hypercube_wavelength.value()][:][:]
      #      test4 = libs_cube.sel(bands=(self.baseline_wavelength.value()/10), method="nearest")
            test4=libs_cube[self.baseline_wavelength.value()][:][:]
            if self.transpose_checkBox.isChecked()==True:          
                img=ax1.imshow(((test.T-test4.T)),interpolation="nearest",cmap=self.colormap_comboBox.currentText())
                fig1.colorbar(img)
            else:
                img=ax1.imshow(((test-test4)),interpolation="nearest", cmap=self.colormap_comboBox.currentText())
                fig1.colorbar(img, ax=ax1)
            print (self.colormap_comboBox.currentText())

        self.canvas = FigureCanvas(fig1)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)
        

    def rmmpl(self,):
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()


    # Handle sys.stdout.write: update text display
    def write(self, text):
        self.text_update.emit(str(text))
 
    def flush(self):
        pass

    # Append to text display
    def append_text(self, text):
        cur = self.textbox.textCursor()     # Move cursor to end of text
        cur.movePosition(QtGui.QTextCursor.End) 
        s = str(text)
        while s:
            head,sep,s = s.partition("\n")  # Split line at LF
            cur.insertText(head)            # Insert text at cursor
            if sep:                         # New line if LF
                cur.insertBlock()
        self.textbox.setTextCursor(cur)     # Update visible cursor

    # Window is closing: stop video capture
    def closeEvent(self, event):
        print("exit asked")
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Sure?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.close()

        else:
            event.ignore()
            
    def open_cube_Dialog(self):
        global fileName
        options = QFileDialog.Options()

        fileName, _ = QFileDialog.getOpenFileName(self,"Open Hypercube", "","NetCDF Files (*.nc);;All Files (*)", options=options)
        if fileName:
            print(fileName)
            self.change_graph(fileName)

if __name__ == '__main__':
        from PyQt5 import QtCore, QtGui, QtWidgets
        from PyQt5.QtWidgets import *
        from PyQt5.QtGui import *
    

        app = QtWidgets.QApplication(sys.argv)
        
   

        win = MainWindow()

        win.setWindowTitle(appname)
        win.setWindowIcon(QIcon('rubiks_cube_15543.ico'))
        
        win.show()
        sys.exit(app.exec_())
