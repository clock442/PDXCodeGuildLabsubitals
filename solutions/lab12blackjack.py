
def blackjack_advice(card1, card2, card3):
    cards = {
        'A': 11,
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
    current_card_list = [card1, card2, card3]
    for element in current_card_list:
        list_of_stuff = list(cards.keys())
        # print(list_of_stuff)
        if element not in list_of_stuff:
            return 'Not valid inputs'
    total = cards[card1] + cards[card2] + cards[card3]
    while True:
        if total < 17:
            return 'Hit'
        elif 16 < total < 21:
            return 'Stay'
        elif total == 21:
            return 'Blackjack!'
        elif total > 21:
            if 'A' in current_card_list:
                current_card_list.remove('A')
                total -= 10
                continue
            else:
                return 'Already busted'
            

while True:
    print('Welcome to Blackjack Advice!')
    print('Your card choices will be 1 to 9 and J, Q, K, A for the rest.')
    card1 = str(input('What is your first card?'))
    card2 = str(input('What is your second card?'))
    card3 = str(input('What is your third card?'))
    print(blackjack_advice(card1, card2, card3))
    repeat = input('Would you like to play again? y/n:   ')
    if repeat == 'n':
        print('Bye Bye')
        break











