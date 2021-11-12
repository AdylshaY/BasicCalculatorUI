import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from calculator2UI import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)


    def hesapla(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Toplama':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        if sender == 'Çıkarma':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        if sender == 'Çarpma':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        if sender == 'Bölme':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())
    
        self.ui.lbl_result.setText(str(result))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())

app()