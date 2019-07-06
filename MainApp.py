"""
This Program is written By Rasika Maduranga
for codechamp 2019
all right received 2019-07-06
"""



import time
import Requester
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import sys
from Gui import Ui_MainWindow


class MainApp:
    """

    Main App controll the GUI And Back End
    GUI Created from pyqt5
    """
    def __init__(self):
        """
        initing the main compoment in QT

        """
        self.back_end = Requester.Doenets()
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyle("Breeze")
        self.mainWin = QMainWindow()

        self.gui = Ui_MainWindow()
        self.text = ""
        self.res = {}
        self.tm = time.time()

    def reset(self):
        """
        Update GUI for given Result

        :return:
        """

        table = self.gui.listWidget_2
        list = self.gui.listWidget

        table.clear()
        table.reset()
        list.clear()
        list.reset()

        i = -1
        """
        Invalid Index catch by name
        """
        if not self.res.get('Name'):
            list.insertItem(0, "Invalid Index")

        for val in self.res:
            if val != 'res':
                i += 1
                list.insertItem(i, val + " : " + self.res[val])
        i = -1
        for subject in self.res["res"]:
            i += 1
            table.insertItem(i, subject + " (" + self.res['res'][subject] + ")")

    def search(self):
        """
        Search Doenets and update GUI

        :return: None
        """

        self.res = self.back_end.read_result(self.gui.lineEdit.text())
        self.reset()

    def run(self):

        """
        connections to gui and start aplication

        """
        self.gui.setupUi(self.mainWin)
        self.gui.pushButton.clicked.connect(self.search)

        self.mainWin.show()
        self.app.exec_()


if __name__ == "__main__":
    """
    Executer 
    
    Initing main app and run
    """
    ma = MainApp()
    ma.run()
