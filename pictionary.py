from PIL import Image, ImageDraw,ImageFont
from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H")
#current_time="10"

#this code generate two photos one for morning time and another for night time

if current_time > "19" and current_time < "7":
    im = Image.new('RGB', (720, 720),(50,54,57) )
    draw = ImageDraw.Draw(im)
else:
    im = Image.new('RGB', (720, 720),(250,214,165) )
    draw = ImageDraw.Draw(im)

## G
draw.ellipse((50, 50, 52, 52), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 70, 52, 72), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 90, 52, 92), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 110, 52, 112), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 130, 52, 132), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 150, 52, 152), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 170, 52, 172), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 190, 52, 192), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 210, 52, 212), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 230, 52, 232), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 250, 52, 252), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((50, 270, 52, 272), fill=(255, 255,255), outline=(99,181,33))


draw.ellipse((70, 250, 72, 252), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((90, 230, 92, 232), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((110, 210, 130, 212), fill=(255, 255,255), outline=(99,181,33))

draw.ellipse((130, 210, 132, 212), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((130, 230, 132, 232), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((130, 250, 132, 252), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((130, 270, 132, 272), fill=(255, 255,255), outline=(99,181,33))



draw.ellipse((50, 50, 52, 52), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((70, 70, 72, 72), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((110, 110, 112, 112), fill=(255, 255,255), outline=(99,181,33))
draw.ellipse((90, 90, 92, 92), fill=(255, 255,255), outline=(99,181,33))

#--------------------------------
# for
## ((left,up,right,down)) f
draw.line((170, 210, 200, 210), fill=(99,181,33),width=2)
draw.line((170, 210, 170, 272), fill=(99,181,33),width=2)
draw.line((170, 235, 200, 235), fill=(99,181,33),width=2)


#o
draw.line((240, 235, 270, 235), fill=(99,181,33),width=2)
draw.line((240, 235, 240, 270), fill=(99,181,33),width=2)
draw.line((270, 235, 270, 270), fill=(99,181,33),width=2)
draw.line((240, 270, 270, 270), fill=(99,181,33),width=2)

#R
draw.line((310, 210, 310, 272), fill=(99,181,33),width=2)
draw.rectangle((310,210,340,240),outline=(99,181,33),width=2)
draw.line((310, 235, 340, 272), fill=(99,181,33),width=2)
#--------------------------------




#G
draw.line((380, 50, 380, 272), fill=(99,181,33),width=2)
draw.line((380, 50, 450, 110), fill=(99,181,33),width=2)
draw.line((380, 272, 450, 212), fill=(99,181,33),width=2)

draw.line((450, 212, 450, 272), fill=(99,181,33),width=2)
#moon




draw.line((0,500,720,500), fill=(250,214,15), width=5)
draw.rectangle((0,550,720,720),fill=(0, 192, 192))
draw.chord((-150,400,600,720), start=180, end=360, fill=(240, 131, 69),outline=(255, 255, 255))
            # ((left,up,right,down))
draw.rectangle((665,150,670,550),fill=(175, 95, 13))
draw.rectangle((640,155,695,157),fill=(175, 95, 13))
draw.rectangle((650,160,685,163),fill=(175, 95, 13))
draw.rectangle((660,166,675,169),fill=(175, 95, 13))
#draw.ellipse((590,100,600,650))
draw.chord((150,450,870,670), start=180, end=360, fill=(240, 131, 69),outline=(255, 255, 255))
gm =ImageFont.truetype(r"C:\Users\kamal\Desktop\whatsapp\Networld-3zRwp.ttf",72)
fnt = ImageFont.truetype(r"C:\Users\kamal\Desktop\whatsapp\FuzzyLogicP2Regular-ZxmJ.ttf", 42)
sgn=ImageFont.truetype(r"C:\Users\kamal\Desktop\whatsapp\Halimun-W7jn.ttf", 33)
cur = now.strftime("%H:%M:%S")
tm=ImageFont.truetype(r"C:\Users\kamal\Desktop\whatsapp\NixiesRegular-anra.ttf",30)
if current_time > "19" and current_time < "7":
    draw.rectangle((0,550,720,720),fill=(76,95,97))
    draw.ellipse((200, 100, 300, 200), fill=(255,255,255))
    draw.text((3,565), "Hello Geeks_For_Geeks!",font=fnt,fill=(99,181,33))
    draw.text((3,610), "Good Night",font=gm,fill=(99,181,33))
    draw.text((550,620), cur,font=tm,fill=(99,181,33))
    draw.text((390,680), "Kamal Swami",font=sgn,fill=(99,181,33))
else:
    draw.ellipse((200, 100, 300, 200), fill=(252,232,3), outline=(255, 255, 255))
    draw.ellipse((205, 105, 295, 195), fill=(241,134,67))
    draw.ellipse((210, 110, 290, 190), fill=(250,79,5))
    draw.text((3,565), "Hello Geeks_For_Geeks!",font=fnt,fill=(255,255,255))
    draw.text((3,610), "Good Morning",font=gm,fill=(255,255,255))
    draw.text((550,620), cur,font=tm,fill=(255,255,255))
    draw.text((390,680), "Kamal Swami",font=sgn,fill=(255,255,255))


im.save(r'pillow_imagedraw.jpg', quality=100)
im.show(r'pillow_imagedraw.jpg')