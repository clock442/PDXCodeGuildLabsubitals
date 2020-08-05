cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def blackjack_advice(card1, card2):
    total = cards[card1] + cards[card2]
    if total < 17:
        return 'Hit'
    elif 16 < total < 21:
        return 'Stay'
    elif total == 21:
        return 'Blackjack!'
    else:
        return 'Already Busted'

while True:
    print('Welcome to Blackjack Advice!')
    print('Your card choices will be 1 to 9 and J, Q, K, A for the rest.')
    card1 = str(input('What is your first card?'))
    card2 = str(input('What is your second card?'))
    print(blackjack_advice(card1, card2))
    repeat = input('Would you like to play again? y/n:   ')
    if repeat == 'n':
        print('Bye Bye')
        break











