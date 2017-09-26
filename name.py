#Claire Yegian
#9/26/17
#name.py - user's name in front of color

from ggame import *

name = input('Enter your name: ')
RGB = input('Enter an RGB code: ')

color = Color('0x'+RGB,1)
black = Color(0x000000,1)

noOutline = LineStyle(0,black)

Rectangle = RectangleAsset(9000,9000,noOutline,color)
text = TextAsset(name, fill=black, style='bold 40pt Times')

Sprite(Rectangle)
Sprite(text,(400,300))
App().run()