import random
eyes = ['=', ';', ':','8',]
nose = [' ', '-', '^', '>',]
mouth = ['O', 'I', '0', '[', ']', ')', '(', '}', '{', '/', 'l']

x = True
while x:
    question = input('Would you like to make 5 random faces? y/n:   ')
    if question == 'y':
        i = 0
        while i < 5:
            print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
            i += 1
    playagain = input('Would you like to play again? y/n:    ')
    if playagain == 'n':
        print('Bye Bye.')
        x = False
