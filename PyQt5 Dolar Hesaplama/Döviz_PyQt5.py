from PyQt5 import QtWidgets, QtGui
import requests
import sys
url = "http://data.fixer.io/api/latest?access_key=43860500edcc6c6935b3651f6f76cbaa"



response = requests.get(url)
veri = response.json()

a = veri["rates"]["USD"]
b = veri["rates"]["TRY"]

c = b / a





class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.setWindowTitle(" Dolar Hesaplama - 1.0 ")
        self.setWindowIcon(QtGui.QIcon('dolar_icon.png'))


        self.dolar_yazisi = QtWidgets.QLabel("Dolar Hesaplama")
        self.yazi_alani = QtWidgets.QSpinBox()
        self.yazi_alani.setMaximum(1_000_000_000)
        self.hesapla = QtWidgets.QPushButton("Hesapla")
        self.goster = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.dolar_yazisi)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.hesapla)
        v_box.addWidget(self.goster)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()




        self.dolar_yazisi.setFont(QtGui.QFont('SansSerif',13))

        self.setLayout(h_box)
        self.setFixedSize(450,150)
        # self.setGeometry(450,250,450,150)

        self.hesapla.clicked.connect(self.dolar_hesapla)



        self.show()

    def dolar_hesapla(self):
        dolar = self.yazi_alani.value()
        
        sonuc = c * dolar
        #print(sonuc)
        sonuc = round(sonuc,2)
        self.goster.setText(str(sonuc))
        
        self.goster.setFont(QtGui.QFont('SansSerif',13))

        
        

app =  QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
