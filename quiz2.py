#Claire Yegian
#9/26/17
#quiz.py - tells user about 2 numbers

num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

if num1==num2:
    print('Your numbers are equal')
elif num1>num2:
    print(num1, 'is greater than', num2)
else:
    print(num2, 'is greater than', num1)
if num1%3==0:
    if num2%3==0:
        print('Both numbers are divisible by 3')
    else:
        print(num1, 'is divisible by 3')
elif num2%3==0:
    print(num2, 'is divisible by 3')
else:
    print('Neither is divisible by 3')

product = float(input('Enter the product of your two numbers: '))

if product==(num1*num2):
    print('Correct')
elif product!=(num1*num2):
    print('Incorrect')
