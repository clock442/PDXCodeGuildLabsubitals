x = True
while x == True:
    grade_number = input('What is your grade percentage as a whole number?: ')
    grade_number = int(grade_number)
    if grade_number < 60:
        print('You got an F.')
    elif grade_number < 64:
        print('You got a D-')
    elif grade_number < 68:
        print('You got a D')
    elif grade_number < 70:
        print('You got a D+')
    elif grade_number < 74:
        print('You got a C-')
    elif grade_number < 78:
        print('You got a C')
    elif grade_number < 80:
        print('You got a C+')
    elif grade_number < 84:
        print('You got a B-')
    elif grade_number < 88:
        print('You got a B')
    elif grade_number < 90:
        print('You got a B+')
    elif grade_number < 94:
        print('You got a A-')
    elif grade_number < 98:
        print('You got a A')
    elif grade_number <= 100:
        print('You got a A+')
    y = input('Would you like to play again? y/n: ')
    if y == 'n':
        x = False