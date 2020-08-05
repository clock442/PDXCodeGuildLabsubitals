coins = [
    ('quarters', 25),
    ('dimes', 10),
    ('nickels', 5),
    ('pennies', 1)
]
while True:
    coin_amounts = []
    total_cents = float(input('Enter a dollar amount:   '))*100
    total_cents = round(total_cents)
    for i in range(len(coins)):
        current_coin_value = coins[i][1]
        if total_cents >= current_coin_value:
            num_coins = total_cents//current_coin_value
            coin_amounts.append(num_coins)
            total_cents -= current_coin_value*num_coins
        else:
            coin_amounts.append(0)
    print('You have:')
    for j in range(len(coin_amounts)):
        print(f'{int(coin_amounts[j])} {coins[j][0]}')
    repeat = input('Would you like to make more change? y/n:   ')
    if repeat != 'y':
        print('Bye Bye')
        break