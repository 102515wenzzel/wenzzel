import sys,os
from PIL import Image, ImageDraw, ImageFont

os.chdir("C:\\work\\python\\wenzzel\\python-master\\acwong00\\0000")
original = Image.open("acwong.jpg")

fnt = ImageFont.truetype("msyh.ttf", 80)

d = ImageDraw.Draw(original)

d.text((200, 0), "8", font=fnt, fill=(255,255,0,255))

original.save("finnal.jpg")

img = Image.open("finnal.jpg")

#グレースケールに変換
gray_img = img.convert("L")

#save
gray_img.save("gray_image.jpg")