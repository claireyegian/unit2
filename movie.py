#Claire Yegian
#9/13/17
#movie.py - how scandalous can you watch?

age = int(input('Enter your age: '))
if age>=18:
    print('You can watch NC-17 rated movies')
elif age>=17:
    print('You can watch R-rated movies')
elif age>=13:
    print('You can watch PG-13 rated movies')
elif age>=8:
    print('You can watch PG-rated movies')
else:
    print('You can watch G-rated movies')
