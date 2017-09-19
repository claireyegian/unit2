#Claire Yegian
#9/19/17
#ageCalculator.py - asks for birthday and gives age

from datetime import date

day1 = int(input('Enter your birth day: '))
month1 = int(input('Enter the number of your birth month: '))
year1 = int(input('Enter your birth year: '))
day2 = int(date.today().day)
month2 = int(date.today().month)
year2 = int(date.today().year)
if month1<month2:
    age1 = year2-year1
    print('You are', age1, 'years old')
elif month1>month2:
    age2 = (year2-year1)-1
    print('You are', age2, 'years old')
elif month1==month2:
    if day1<day2:
        age1 = year2-year1
        print('You are', age1, 'years old')
    elif day1>day2:
        age2 = (year2-year1)-1
        print('You are', age2, 'years old')
    elif day1==day2:
        age1 = year2-year1
        print('Happy birthday!')
        print('You are', age1, 'years old')