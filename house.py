#Claire Yegian
#9/22/17
#house.py - prints house image

from ggame import *

grey = Color(0xc0c0c0,1)
blue = Color(0xccffff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(0,black)

greyRectangle = RectangleAsset(400,200,blackOutline,grey)

Sprite(greyRectangle,(300,200))
App().run()