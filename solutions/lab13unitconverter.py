convert_dict = {
    'ft': {
        'ft': 1,
        'mi': 5280,
        'm': 0.3048,
        'km': 0.0003048
    },
    'mi':{
        'ft': 5280,
        'mi': 1,
        'm': 1609.34,
        'km': 1.60934
    },
    'm':{
        'ft': 3.28084,
        'mi': 0.000621,
        'm': 1,
        'km': 0.001
    },
    'km':{
        'ft': 3280.84,
        'mi': 0.621,
        'm': 1000,
        'km': 1
    }
}

print('Welcome to unit converter. Your available units are ft, mi, m, and km.')
while True:
    unit_from = input('What unit would you like to convert from: ')
    unit_to = input('What unit would you like to convert to: ')
    if unit_from not in list(convert_dict.keys()) or unit_to not in list(convert_dict.keys()):
        print('Not a valid input')
        continue
    distance = float(input('What is your distance: '))
    converted_num = distance * convert_dict[unit_from][unit_to]
    print(f'Your distance in {unit_to} is {converted_num}.')
    repeat = input('Would you like to convert something else? y/n: ')
    if repeat == 'n':
        break