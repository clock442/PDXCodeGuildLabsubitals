import string
#  0 1 2 3 4
# 'a b c d e'
#             0         1         2
# fruits = ['pears', 'bannas', 'graps']

# fruits[1] #bannas

# b 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_rotation = 13



input_text = 'hello'

output_text = ''
for char in input_text:
    char_index = alphabet.find(char)






    output_index = char_index + user_rotation  
    output_index%len(alphabet)
    output_text += alphabet[output_index]





    




print(output_text)