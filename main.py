from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QRunnable, pyqtSlot, QThreadPool, QTimer
from PyQt5.QtWidgets import QApplication

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(258, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 30, 75, 23))
        self.pushButton.setObjectName('pushButton')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.pushButton_2.setObjectName('pushButton_2')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 90, 113, 21))
        self.lineEdit.setObjectName('lineEdit')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 47, 13))
        self.label.setObjectName('label')
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(103, 120, 113, 13))
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(190, 130, 113, 13))
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(66, 130, 120, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setValue(0)
        self.slider.setMaximum(20)
        self.slider.valueChanged.connect(self.setText)

        MainWindow.setCentralWidget(self.centralwidget)
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(90, 150, 75, 23))
        # self.pushButton_3.setObjectName('pushButton_3')
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def setText(self):
        _translate = QtCore.QCoreApplication.translate
        self.label2.setText(str(self.slider.value()))
        return
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'Moldifier'))
        self.pushButton.setText(_translate('MainWindow', 'Open File'))
        self.pushButton_2.setText(_translate('MainWindow', 'Compress'))
        self.label1.setText(_translate("MainWindow", "Iterations"))
        self.label.setText(_translate('MainWindow', 'Filename'))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())