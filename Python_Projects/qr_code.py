import qrcode as qr
img = qr.make("https://www.linkedin.com/in/mittal-chirag/")
img.save("Linkedin.png")
