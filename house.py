#Claire Yegian
#9/22/17
#house.py - prints house image

from ggame import *

grey = Color(0xc0c0c0,1)
darkGrey = Color(0x606060,1)
blue = Color(0xccffff,1)
black = Color(0x000000,1)

blackOutline = LineStyle(0,black)
Outline = LineStyle(1,black)

greyRectangle = RectangleAsset(400,200,blackOutline,grey)
greyTriangle = PolygonAsset([(300,200),(700,200),(500,100)],blackOutline,grey)
door = RectangleAsset(65,100,blackOutline,darkGrey)
window = RectangleAsset(60,60,blackOutline,blue)

Sprite(greyRectangle,(300,200))
Sprite(greyTriangle)
Sprite(door,(460,300))
Sprite(window,(370,250))
App().run()