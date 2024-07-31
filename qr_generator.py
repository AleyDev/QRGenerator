# pyqrcode kütüphanesini içe aktarıyorum, QR kodları oluşturmak için kullanacağım.
import pyqrcode


# Kullanıcıdan QR kodunu oluşturmak için bir URL girmesini istiyorum.
url = input("Enter url to generate qr code: ")

# Kullanıcının girdiği URL'yi kullanarak QR kodunu oluşturuyorum.
qr_code = pyqrcode.create(url)

# Oluşturduğum QR kodunu 'qrcode.svg' adlı bir dosyaya kaydediyorum. scale parametresi ile QR kodunun boyutunu ayarlıyorum.
qr_code.svg("qrcode.svg", scale=5)
