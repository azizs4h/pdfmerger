#developed by azizs4h 

from PyQt5.QtWidgets import QMainWindow, QApplication, QScrollArea, QStatusBar, QSizePolicy,QPushButton,QWidget, QInputDialog, QLineEdit, QFileDialog, QFormLayout, QGroupBox, QLabel, QMessageBox
from PyQt5.QtGui import QCursor, QPixmap, QIcon
from PyQt5.QtCore import QRect, QSize, QMetaObject, Qt, QCoreApplication
from PyPDF2 import PdfFileMerger
from sys import exit

class Ui_MainWindow(object):
    filenames = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        sizePolicy =QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        MainWindow.setIconSize( QSize(48, 48))
        self.centralwidget =QWidget(MainWindow)
        sizePolicy =QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry( QRect(230, 240, 100, 45))
        self.pushButton.setStyleSheet(
            "padding :10px;"
        )
        self.pushButton.setCursor(QCursor( Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry( QRect(350, 240, 100, 45))
        self.pushButton_2.setStyleSheet(
            "padding :10px;"
        )
        self.pushButton_2.setCursor(QCursor( Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry( QRect(30, 50, 421, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents =QWidget()
        self.scrollAreaWidgetContents.setGeometry( QRect(0, 0, 419, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label =QLabel(self.centralwidget)
        self.label.setGeometry( QRect(30, 20, 191, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar =QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate =  QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pdf Birleştirici"))
        self.pushButton.setText(_translate("MainWindow", "Dosya Seç"))
        self.pushButton_2.setText(_translate("MainWindow", "Birleştir"))
        self.label.setText(_translate("MainWindow", "Birleştirilecek olan dosyalar : "))
        self.pushButton.clicked.connect(self.open_dialog_box)
        self.pushButton_2.clicked.connect(self.getDirectory)
        
    def open_dialog_box(self):
        try:
            self.filenames = QFileDialog.getOpenFileNames(MainWindow,"Dosyaları Seçin","","PDF dosyaları (*.pdf)")
            dosyalar = []

            formLayout = QFormLayout()
            groupbox = QGroupBox()

            for i in range(0,len(self.filenames[0])):
                dosyalar.append(QLabel(self.filenames[0][i]))
                formLayout.addRow(dosyalar[i])

            groupbox.setLayout(formLayout)    
            self.scrollArea.setWidget(groupbox)
        except Exception:
            outputDialog = QMessageBox()
            outputDialog.setWindowTitle("Hata")
            outputDialog.setIcon(QMessageBox.Critical)
            outputDialog.setText("Bir hata Oluştu Lütfen Tekrar Deneyiniz")
            outputDialog.exec()
        

    def getDirectory(self):

        if not None == self.filenames:
            fileDirectory = str(QFileDialog.getSaveFileName(MainWindow,"Dosyanın Kaydedileceği Konumu Seçin","output.pdf","PDF dosyaları (*.pdf)")[0])
            try:
                self.merge(fileDirectory)
            except Exception:
                outputDialog = QMessageBox()
                outputDialog.setWindowTitle("Dosya Dizini Seçilmedi")
                outputDialog.setText("İşlem İptal Edildi Lütfen Yeniden Dosya Seçin")
                outputDialog.exec()
        else:
            self.filenames=None
            outputDialog = QMessageBox()
            outputDialog.setWindowTitle("Dosya Seçilmedi")
            outputDialog.setText("Lütfen Birleştirilecek Dosyaları Seçiniz.")
            outputDialog.exec()

    def merge(self,directory):

        if not None == self.filenames:
            merger = PdfFileMerger(strict=False)
            files = self.filenames[0]
            for item in files:
                if item.endswith('pdf'):
                    merger.append(item)
            merger.write(directory)
            merger.close()
            self.filenames = None

            outputDialog = QMessageBox()
            outputDialog.setWindowTitle("Dosya kaydedildi")
            outputDialog.setText("Dosya Başarıyla "+ directory +" Dizinine Kaydedildi")
            outputDialog.exec()

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec_())