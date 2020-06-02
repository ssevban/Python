# pip install pyqrcode
# pip install pypng

# SEVBAN :)


import pyqrcode

veri = "https://github.com/s3vb4n"
url = pyqrcode.create(veri)
url.png("example.png",scale=10)
