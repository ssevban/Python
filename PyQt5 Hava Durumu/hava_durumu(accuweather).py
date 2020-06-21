import feedparser
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtGui import QIcon
parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|10100|BALIKESIR|")
parse = parse["entries"][0]["summary"]
parse = parse.split()
a = parse[4]

def Win():
	app = QtWidgets.QApplication(sys.argv)
	win = QtWidgets.QWidget()
	win.setWindowIcon(QIcon('icon.png'))





	win.setWindowTitle("BALIKESİR HAVA DURUMU")
	win.setFixedSize(350,80)
	etiket = QtWidgets.QLabel(win)
	balkes = QtWidgets.QLabel(win)
	balkes.setText("BALIKESİR")
	balkes.setFont(QtGui.QFont('SansSerif',13))
	de = QtWidgets.QLabel(win)
	de.setText("°C")
	de.setFont(QtGui.QFont('SansSerif',13))
	de.move(160,25)

	etiket.setText(a)
	etiket.move(140,25)
	balkes.move(40,25)
	etiket.setFont(QtGui.QFont('SansSerif',13))
	# win.setGeometry(200,150,400,80)
	win.show()

	sys.exit(app.exec_())



Win()













