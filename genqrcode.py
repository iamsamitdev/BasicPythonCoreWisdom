import qrcode
img = qrcode.make('https://www.itgenius.co.th')
type(img)
img.save("myqrcode.png")