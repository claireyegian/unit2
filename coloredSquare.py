#Claire Yegian
#9/18/17
#coloredSquare.py - gives user a colored square

from ggame import*

from random import randint

num = randint(1,4)

if num == 1:
    red = Color(0xff0000,1)
    line = LineStyle(3,red)
    rectangle = RectangleAsset(100,100,line,red)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
if num == 2:
    darkslategray = Color(0x2f4f4f, 1)
    line = LineStyle(3,darkslategray)
    rectangle = RectangleAsset(100,100,line,darkslategray)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
    