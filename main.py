from randommons import *
from friigooi import *
import sys
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QIcon, QPixmap
n = 0
count = 0
counter = 0 
def file_save():
    global a 
    options = QFileDialog.Options()
    fileName = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    try:
        f = open(fileName[0], "x")
        try:
            f.write(a[0] + a[1] + a[2] + a[3] + a[4] + a[5])
        except:
            pass
        finally:
            f.close()
    except:
        pass
def createactual():
    global a, counter 
    a = createTeam("a")
    counter += 1 
    if str(counter)[-1] == "1" and counter != 11:
        ui.label_3.setText(str("Current team"+":"+str(counter)+"st"))
    elif str(counter)[-1] == "2" and counter != 12:
        ui.label_3.setText(str("Current team"+":"+str(counter)+"nd"))
    else:
        ui.label_3.setText(str("Current team"+":"+str(counter)+"th"))
def stpactual():
    global a,counter 
    try:
        b = savetoPokepastes(a)
        ui.lineEdit.setText(b)
        if str(counter)[-1] == "1" and counter != 11:
            ui.label_2.setText(str("Current url"+"\n"+"("+str(counter)+"st"+")"))
        elif str(counter)[-1] == "2" and counter != 12:
            ui.label_2.setText(str("Current url"+"\n"+"("+str(counter)+"nd"+")"))
        else:
            ui.label_2.setText(str("Current url"+"\n"+"("+str(counter)+"th"+")"))
    except:
        pass
def clipcopy():
    clipboard = QtWidgets.QApplication.clipboard()
    try:
        clipboard.setText(ui.lineEdit.text())
    except:
        pass
def settheme():
    global count,n
    if count % 5 == 0:
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/red.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("red.png"))
        count += 1
    elif count % 5 == 1:
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/blue.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("blue.png"))
        count += 1
    elif count % 5 == 2:
        count += 1
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/black.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("black.png"))
    elif count % 5 == 3: 
        count += 1
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/green.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("green.png"))
    elif count % 5 == 4 and count != 69:
        count += 1
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/white.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("white.png"))
    elif count == 69:
        count += 1
        try:
            ui.label.setPixmap(QtGui.QPixmap("resources/blobaww.png"))
        except:
            ui.label.setPixmap(QtGui.QPixmap("blobaww.png"))
       
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.label.setScaledContents(True)
timer = QtCore.QTimer()
time = QtCore.QTime(0, 0, 0)
timer.timeout.connect(lambda: ui.dynamicaww(MainWindow))
timer.start(100)
ui.pushButton_4.clicked.connect(lambda: createactual())
ui.pushButton.clicked.connect(lambda: file_save())
ui.pushButton_2.clicked.connect(lambda: stpactual())
ui.pushButton_3.clicked.connect(lambda: clipcopy())
ui.pushButton_5.clicked.connect(lambda: settheme())
sys.exit(app.exec_())
