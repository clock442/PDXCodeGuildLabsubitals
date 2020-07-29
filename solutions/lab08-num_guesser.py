import random
import string

while True:
    print('Welcome to number guesser. You have 10 attempts to guess my number which is between 1 and 100.')
    comp_choice = random.randint(0, 100)
    attempts = 1
    hum_choice = 0
    last_guess = hum_choice
    last_difference = 0
    difference = abs(comp_choice - hum_choice)
    while attempts <= 10:
        hum_choice = input('Guess a number:   ')
        hum_choice = int(hum_choice)
        difference = abs(hum_choice - comp_choice)
        if hum_choice == comp_choice:
            print('You guessed correctly!')
            attempts = 11
        elif hum_choice < comp_choice or hum_choice > comp_choice:
            print(f'You have made {attempts} atempts.')
            if last_difference == 0:
                print('That was your first guess.')
            elif difference > 0:
                if difference < last_difference:
                    print('You are getting warmer.')
                elif difference > last_difference:
                    print('You are getting colder.')
                else:
                    continue

        last_difference = difference
        attempts += 1
    if attempts == 10:
        print('That was all of your guesses. You lose.')
    play_again = input('Would you like to play again? y/n:    ')
    if play_again == 'n':
        print('Bye Bye')
        break
    else:
        attempts = 1



    


