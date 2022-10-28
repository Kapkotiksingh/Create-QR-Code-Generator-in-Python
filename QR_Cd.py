import qrcode as qr


img = qr.make("https://www.youtube.com/channel/UCz9max38aizoaWZVRH_omLg")
img.save("kamal_youtube.png")