#Claire Yegian
#9/14/17
#compoundConditionalDemo.py - and/or

num = float(input('Enter a number: '))

if num>0 and num%7==0:
    print('Your number is positive and divisible by seven')
elif num>0:
    print('Your number is positive and not divisible by seven')
elif num<0 and num%7==0:
    print('Your number is negative and divisible by seven')
elif num<0:
    print('Your number is negative and not divisible by seven')
else:
    print('Your number is zero')
