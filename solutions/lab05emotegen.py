import random
eyes = ['=', ';', ':','8',]
nose = [' ', '-', '^', '>',]
mouth = ['O', 'I', '0', '[', ']', ')', '(', '}', '{', '/', 'l']

x = True
while x:
    question = input('Would you like to make a random face? y/n:   ')
    if question == 'y':
        print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
    playagain = input('Would you like to play again? y/n:    ')
    if playagain == 'n':
        print('Bye Bye.')
        x = False
