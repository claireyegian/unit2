#Claire Yegian
#9/18/17
#adventure.py - mimics 1976 computer game Adventure

river = input('A bear is chasing you. You come to a river. Do you jump in the river? ')
if river == 'yes':
    punch = input('Thankfully, you know how to swim. However, you notice a nearby shark. Do you punch it in the nose? ')
    if punch == 'yes':
        print('The shark eats you and you die')
    elif punch == 'no':
        print('You manage to swim to the other shore and go on to live a long, happy life with your 87 cats')
elif river == 'no':
    climb = input('You see a tree on the bank of the river. Do you climb the tree? ')
    if climb == 'yes':
        print('You forgot to consider that bears can climb really well. The bear catches up to you easily and eats you alive')
    elif climb == 'no':
        print('Youre kind of stuck, so the bear eats you anyway')
