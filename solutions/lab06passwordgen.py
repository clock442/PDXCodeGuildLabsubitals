import random
import string

x = True
while x:
    play = input('Would you like to generate a password? y/n:   ')
    while play == 'y':
        pass_length = int(input('How many characters would you like your password to be?:    '))
        password = []
        for char in range(pass_length + 1):
            password += random.choice([random.choice(string.ascii_letters), random.choice(string.digits), random.choice(string.punctuation)])
        password = ''.join(password)
        print(f'This is your new password: {password}')
        play_again = input('Would you like to play again? y/n:    ')
        if play_again == 'n':
            play = False
            x = False