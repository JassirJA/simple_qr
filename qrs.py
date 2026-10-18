import qrcode
import os

url = input("Enter URL:").strip()
file_path = os.path.dirname(os.path.abspath(__file__)) + "\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
