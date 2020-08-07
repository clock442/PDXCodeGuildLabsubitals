while True:
    under_twenty = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    tens_place = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }
    user_num = int(input('What is your number: '))
    tens_digit = str(user_num//10)
    ones_digit = str(user_num%10)
    if user_num < 20:
        user_string = str(user_num)
        if user_string in under_twenty:
            print(under_twenty[user_string])
    elif user_num > 19:
        if ones_digit != '0':
            print(f'{tens_place[tens_digit]}-{under_twenty[ones_digit]}')
        else:
            print(tens_place[tens_digit])
    else:
        print('Not valid')
    repeat = input('Would you like to convert something else? y/n: ')
    if repeat == 'n':
        print('Bye Bye')
        break        