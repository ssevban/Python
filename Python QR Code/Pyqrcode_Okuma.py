# pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image
d = decode(Image.open('example.png'))
print(d[0].data.decode('ascii'))
