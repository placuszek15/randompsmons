from randommons import *
from friigooi import *
import sys
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QIcon, QPixmap
n = 0
count = 0
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
    global a 
    a = createTeam("a") 
def stpactual():
    global a 
    try:
        b = savetoPokepastes(a)
        #ui.lineEdit.setReadOnly(False)
        ui.lineEdit.setText(b)
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
        ui.label.setPixmap(QtGui.QPixmap("white.png"))
        count += 1
    elif count % 5 == 1:
        ui.label.setPixmap(QtGui.QPixmap("black.png"))
        count += 1
    elif count % 5 == 2:
        count += 1
        ui.label.setPixmap(QtGui.QPixmap("red.png"))
    elif count % 5 == 3: 
        count += 1
        ui.label.setPixmap(QtGui.QPixmap("blue.png"))
    elif count % 5 == 4 and count != 69:
        count += 1
        ui.label.setPixmap(QtGui.QPixmap("green.png"))
    elif count == 69:
        count += 1
        ui.label.setPixmap(QtGui.QPixmap("blobaww.png"))
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

MainWindow.show()
ui.label.setScaledContents(True)
ui.pushButton_4.clicked.connect(lambda: createactual())

ui.pushButton.clicked.connect(lambda: file_save())
ui.pushButton_2.clicked.connect(lambda: stpactual())
ui.pushButton_3.clicked.connect(lambda: clipcopy())
ui.pushButton_5.clicked.connect(lambda: settheme())
sys.exit(app.exec_())
