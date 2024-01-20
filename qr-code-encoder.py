import qrcode

data_encoded = 'Hello World!'#encode the qrcode with data
img = qrcode.make(data_encoded)
img.save('C:/Users/Zawadi/Desktop/python-projects/qrcode-img/helloWorld.png')#any time you are working with directories in python, we change the back slash to a front slash