import qrcode

img_qrcode = qrcode.make("https://www.linkedin.com/in/j%C3%A9sus-teixeira-63345811a/")
img_qrcode.save("qrcode_py.png")
