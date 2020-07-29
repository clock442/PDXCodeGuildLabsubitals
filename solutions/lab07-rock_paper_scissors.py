import random
choice = ['rock','paper','scissors']
def rand_comp_choice():
    cchoice = random.choice(choice)
    return cchoice


x = True
while x == True:
    print('Lets play rock, paper, scissors')
    player_choice = input('Choose rock, paper, or scissors.:   ')
    player_choice = player_choice.lower()
    if player_choice in choice:
        comp_hand = rand_comp_choice()
        print(f'The computer chose {comp_hand}.')
        result = ''
        if player_choice == 'rock':
            if comp_hand == 'scissors':
                result = 'You won!'
            elif comp_hand == 'paper':
                result = 'You lost'
            elif comp_hand == 'rock':
                result = 'We tied.'
        elif player_choice == 'paper':
            if comp_hand == 'rock':
                result = 'You won!'
            elif comp_hand == 'scissors':
                result = 'You lost'
            elif comp_hand == 'paper':
                result = 'We tied.'
        elif player_choice == 'scissors':
            if comp_hand == 'paper':
                result = 'You won!'
            elif comp_hand == 'rock':
                result = 'You lost'
            elif comp_hand == 'scissors':
                result = 'We tied.'
    else:
        print('Please make a valid choice.')
        continue
    print(result)
    play_again = input('Would you like to play again? y/n:   ')
    if play_again == 'n':
        x = False
print('Bye Bye')
    





 