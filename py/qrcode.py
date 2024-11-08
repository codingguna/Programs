import qrcode
data="C:\Users\gs400\Pictures\bank account.jpg"
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("C:\\Users\\gs400\\Documents\\gunainsta.png")
