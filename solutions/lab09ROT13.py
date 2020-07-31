import string
alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+/[]<>?`;:"~*'

def rot(text):

    rotation = int(input('How many letters would you like to rotate the alphabet and special characters:    '))%52
    new_list = []
    text = text.lower()
    for letter in text:
        if letter == ' ':
            new_list.append(' ')
        for rot_letter in alphabet:
            if letter == rot_letter:
                new_list.append(alphabet[alphabet.find(rot_letter) - rotation])

    new_string = ''.join(new_list)
    return new_string

while True:
    print('ROT encodes words you give it by rotating the alphabet and special characters.')
    user_text = input('Type:   ')
    print(rot(user_text))
    play_again = input('Would you like to encode more? y/n:   ')
    if play_again == 'n':
        print('Bye Bye')
        break
