#Claire Yegian
#9/18/17
#warmUp.py - find 7 or divisible by 7 game

num = int(input('Enter a number: '))
if '7' in str(num) or num%7==0:
    print('Buzz')
else:
    print(num)