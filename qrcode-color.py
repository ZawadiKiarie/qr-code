import qrcode
from PIL import Image

data = 'Hello Barbie!'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 2)#create an instance of qrcode from qrcode class and intialize
qr.add_data(data)#add data to the qrcode we want tor create
qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color='pink')
img.save('C:/Users/Zawadi/Desktop/python-projects/qrcode-img/helloWorld1.png')