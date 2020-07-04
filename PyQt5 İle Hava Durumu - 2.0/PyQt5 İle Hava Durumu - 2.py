#coding=utf8
# -*- coding: utf-8 -*-
import feedparser
from PyQt5 import QtWidgets,QtGui
import sys
balikesir_sicaklik = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|10100|BALIKESIR|")
ankara_sicaklik = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|06010|ANKARA|")
istanbul_sicaklik = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34010|ISTANBUL|")
balikesir_sicaklik = balikesir_sicaklik["entries"][0]["summary"]
ankara_sicaklik = ankara_sicaklik["entries"][0]["summary"]
istanbul_sicaklik = istanbul_sicaklik["entries"][0]["summary"]
balikesir_sicaklik = balikesir_sicaklik.split()
ankara_sicaklik = ankara_sicaklik.split()
istanbul_sicaklik = istanbul_sicaklik.split()
balikesir_sicaklik = balikesir_sicaklik[4]
ankara_sicaklik = ankara_sicaklik[4]
istanbul_sicaklik = istanbul_sicaklik[4]

class Pencere(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()
	def init_ui(self):
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.sicaklik_gostergesi = QtWidgets.QLabel()
		self.sehir_ismi = QtWidgets.QLabel()
		self.derece_isareti = QtWidgets.QLabel()
		self.combo_box  = QtWidgets.QComboBox()
		self.buton = QtWidgets.QPushButton("Göster")
		self.combo_box.addItems(["Seçiniz","İstanbul","Balıkesir","Ankara"])
		v_box = QtWidgets.QVBoxLayout()
		v_box.addStretch()
		v_box.addWidget(self.combo_box)
		v_box.addWidget(self.buton)
		v_box.addStretch()
		h_box = QtWidgets.QHBoxLayout()
		# h_box.addWidget(self.combo_box)
		# h_box.addWidget(self.buton)
		h_box.addStretch()
		h_box.addLayout(v_box)
		h_box.addStretch()
		h_box.addWidget(self.sehir_ismi)
		h_box.addWidget(self.sicaklik_gostergesi)
		h_box.addWidget(self.derece_isareti)
		h_box.addStretch()
		self.setLayout(h_box)
		self.buton.clicked.connect(self.hava_durumu_gostergesi)
		self.setWindowTitle("Hava Durumu - 2.0")
		self.show()
		self.setFixedSize(450,150)
	def hava_durumu_gostergesi(self):
		if self.combo_box.currentText() == "İstanbul":
			self.sehir_ismi.setText("İstanbul ")
			self.sicaklik_gostergesi.setText(istanbul_sicaklik)
			self.derece_isareti.setText("°C")
		elif self.combo_box.currentText() == "Balıkesir":
			self.sehir_ismi.setText("Balıkesir ")
			self.sicaklik_gostergesi.setText(balikesir_sicaklik)
			self.derece_isareti.setText("°C")
		elif self.combo_box.currentText() == "Ankara":
			self.sehir_ismi.setText("Ankara")
			self.sicaklik_gostergesi.setText(ankara_sicaklik)
			self.derece_isareti.setText("°C")
		elif self.combo_box.currentText() == "Seçiniz":
			self.sehir_ismi.setText("LÜTFEN GEÇERLİ BİR ŞEHİR SEÇİNİZ")
			self.sicaklik_gostergesi.setText(" ")
			self.derece_isareti.setText(" ")
                

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
