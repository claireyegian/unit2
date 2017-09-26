#Claire Yegian
#9/26/17
#germany.py - prints german flag

from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xFFFF33,1)
black = Color(0x000000,1)

noOutline = LineStyle(0,black)

blackRectangle = RectangleAsset(400,80,noOutline,black)
redRectangle = RectangleAsset(400,80,noOutline,red)
yellowRectangle = RectangleAsset(400,80,noOutline,yellow)

Sprite(blackRectangle)
Sprite(redRectangle,(0,80))
Sprite(yellowRectangle,(0,160))
App().run()