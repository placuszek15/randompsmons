# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frigam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Random PS Hackmons")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 451))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 260, 141, 20))
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 290, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 80, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 260, 81, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(414, 30, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400,95,80,20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Hackmons Generator"))
        self.pushButton.setText(_translate("MainWindow", "Save to txt"))
        self.pushButton_2.setText(_translate("MainWindow", "Save to pokepast.es"))
        self.pushButton_3.setText(_translate("MainWindow", "Copy url"))
        self.pushButton_4.setText(_translate("MainWindow", "Create team!"))
        self.label_2.setText(_translate("MainWindow", "Current url"))
        self.pushButton_5.setText(_translate("MainWindow", "Change theme"))
        self.label_3.setText(_translate("MainWindow", "Current team"))
    def dynamicaww(self, MainWindow):
        w = MainWindow.frameGeometry().width()
        h = MainWindow.frameGeometry().height()
        self.label.setGeometry(QtCore.QRect(0, 0, w, h))
        self.lineEdit.setGeometry(QtCore.QRect(round(w/(500/190)), round(h/(430/260)), round(w/(500/160)), round(h/(430/20))))
        self.pushButton.setGeometry(QtCore.QRect(round(w/(500/130)), round(h/(430/220)), round(w/(500/111)),  round(h/(430/31))))
        self.pushButton_2.setGeometry(QtCore.QRect(round(w/(500/270)),round(h/(430/220)), round(w/(500/111)),  round(h/(430/31))))
        self.pushButton_3.setGeometry(QtCore.QRect(round(w/(500/190)),round(h/(430/290)), round(w/(500/151)),  round(h/(430/31))))
        self.pushButton_4.setGeometry(QtCore.QRect(round(w/(500/130)),round(h/(430/80)), round(w/(500/251)),  round(h/(430/111))))
        self.label_2.setGeometry(QtCore.QRect(round(w/(500/100)), round(h/(430/260)), round(w/(500/81)),  round(h/(430/41))))
        self.pushButton_5.setGeometry(QtCore.QRect(round(w/(500/400)), round(h/(430/30)), round(w/(500/91)),  round(h/(430/31))))
        self.label_3.setGeometry(QtCore.QRect(round(w/(500/400)), round(h/(430/95)),90,20))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(lambda: ui.dynamicaww(MainWindow))
    timer.start(100)
    MainWindow.show()
    sys.exit(app.exec_())
