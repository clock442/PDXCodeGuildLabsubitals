import string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rot(text):

    new_list = []
    text.lower()
    for letter in text:
        # new_list.append(text[letter] 
        for rot_letter in alphabet:
            if letter == rot_letter:
                new_list.append(alphabet[alphabet.find(rot_letter) - rotation])
    new_string = ''.join(new_list)
    return new_string

while True:
    print('ROT encodes words you give it by rotating the alphabet.')
    rotation = int(input('How many letters would you like to rotate the alphabet:    '))
    user_text = input('Type words:   ')
    print(rot(user_text))
    play_again = input('Would you like to encode more? y/n:   ')
    if play_again == 'n':
        print('Bye Bye')
        break
