import string
coins = [25, 10, 5, 1]
while True:
    coin_amounts = [0, 0, 0, 0]
    total_cents = float(input('Enter a dollar amount:   '))*100
    for i in range(len(coins)):
        if total_cents >= coins[i]:
            num_coins = total_cents//coins[i]
            coin_amounts[i] += num_coins
            total_cents -= coins[i]*num_coins
    print(f'You would have {int(coin_amounts[0])} quarters, {int(coin_amounts[1])} dimes, {int(coin_amounts[2])} nickels, and {int(coin_amounts[3])} pennies.')
    repeat = input('Would you like to make more change? y/n:   ')
    if repeat != 'y':
        print('Bye Bye')
        break