#Claire Yegian
#9/19/17
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #horizontal_radius, vertical_radius, outline, fill

Sprite(redRectangle)
Sprite(blueCircle,(50,50)) #Sprite(Circle, (point))
Sprite(greenEllipse, (200,400))
App().run()











