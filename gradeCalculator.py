#Claire Yegian
#9/13/17
#gradeCalculator.py - calculates grade

grade = float(input('Enter your grade: '))
if grade>=90:
    print('You earned an A')
elif grade>=80:
    print('You earned a B')
elif grade>=70:
    print('You earned a C')
elif grade>=60:
    print('You earned a D')
else:
    print('You earned an F')
