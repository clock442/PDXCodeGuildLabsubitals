x = True
while x == True:
    print('Mad Lib')
    place1 = input('Give me a place. ')
    color2 = input('Give me a color. ')
    name3 = input('Give me a name. ')
    verb4 = input('Give me a verb. ')
    noun5 = input('Give me a noun. ')

    print(f'{name3} was walking to the {place1} when all of a suden they heard a loud noise.\n{name3} turned around to see a giant {color2} {noun5}. When {name3} saw it, {name3} started {verb4}ing. The end.')
    y = input('Would you like to play again?: y/n')
    if y == 'n':
        x = False