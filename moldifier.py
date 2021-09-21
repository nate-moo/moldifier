from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QFileDialog, QApplication
from tempfile import TemporaryDirectory
from PIL import Image
from main import Ui_MainWindow
from pathlib import Path
import sys
import os
from subprocess import Popen

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnPushButton)
        self.ui.pushButton_2.clicked.connect(self.btnPushButton2)
        # self.ui.actionSize_Targeter.clicked.connect(self.)
        self.filePath = ""

    def btnPushButton(self):
        print("hello")
        dialog = QFileDialog.getOpenFileName()
        print(f"{dialog[0]}")
        self.filePath = dialog[0]
    
    def btnPushButton2(self):
        path = os.path.split(f"{self.filePath}")[0]

        if self.ui.img.isChecked():   
            img = Image.open(self.filePath)
            imgExport = self.ui.lineEdit.text()
            if self.ui.slider.value() != 0:
                with TemporaryDirectory(dir=path) as tempDir:
                    print(f"Temp Dir: {tempDir}")
                    for a in range(self.ui.slider.value()):
                        print(a)
                        print(f"Image Size: {img.size}")
                        img = img.convert("RGB")
                        t = a
                        if a == 0:
                            img.save(f"{tempDir}/{a}-{imgExport}", optimize=True, quality=1)
                        else:
                            imga = Image.open(f"{tempDir}/{a-1}-{imgExport}")
                            imga.save(f"{tempDir}/{a}-{imgExport}", optimize=True, quality=1)
                    print(t)
                    os.rename(f"{tempDir}/{t}-{imgExport}", f"{imgExport}")
            else:
                print(f"Image Size: {img.size}")
                img = img.convert("RGB")
                img.save(imgExport, optimize=True, quality=1)
                print("done")
        else:
            if self.ui.slider.value() != 0:
                with TemporaryDirectory(dir=path) as tempDir:
                    print(f"Temp Dir: {tempDir}")
                    t = 0
                    for a in range(self.ui.slider.value()):
                        print(a)
                        if a == 0:
                            Popen([resource_path("ffmpeg.exe"), "-i", self.filePath, "-b:v", "20k", "-b:a", "10k", "-preset", "ultrafast", f"{tempDir}/{a+1}-{self.ui.lineEdit.text()}"], shell=True).wait()
                        else:
                            t = a
                            Popen([resource_path("ffmpeg.exe"), "-i", f"{tempDir}/{a}-{self.ui.lineEdit.text()}", "-b:v", "20k", "-b:a", "10k", "-preset", "ultrafast", f"{tempDir}/{a+1}-{self.ui.lineEdit.text()}"], shell=True).wait()
                    os.rename(f"{tempDir}/{t}-{self.ui.lineEdit.text()}", f"{path}/{self.ui.lineEdit.text()}")
            else:
                print("goodbye")
                print(f"{self.filePath}")
                print(f"{path}/{self.ui.lineEdit.text()}")
                Popen([resource_path("ffmpeg.exe"), "-i", self.filePath, "-b:v", "10k", "-b:a", "5k", "-preset", "ultrafast", f"{path}/{self.ui.lineEdit.text()}"], shell=True).wait()


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec())