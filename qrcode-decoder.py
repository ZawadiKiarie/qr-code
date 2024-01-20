from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Zawadi/Desktop/python-projects/qrcode-img/helloWorld.png')#what image we want to get the data of
result = decode(img)
print(result)
#it's not a must it be a qrcode that you created, you can decode a qrcode you found online