import requests
import string
import re
import math

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('book.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# finding every word in the text and putting it in a list
txt_word_list = re.findall(r"\s?\w+'?\w*\s+", text)
# making all of the words lowercase with no white space
fixed_word_list = []
for word in txt_word_list:
    fixed_word_list.append(word.lower().strip())

# find total characters in the text
total_chars = 0
for item in fixed_word_list:
    total_chars += len(item)

# find total words in text
total_words = len(fixed_word_list)

# find total sentences in text
sentence_list = re.findall(r"\s+[^.!?]*[.!?]", text)
total_sentences = len(sentence_list)

ari = math.floor((4.71 * (total_chars/total_words)) + (0.5 *(total_words/total_sentences))-21.43)

print(f'The ARI for the text is {ari}')
print('This corresponds to a ' + ari_scale[ari]['grade_level'] + 'level of dificulty.')
print('That is suitable for an average person of ' +ari_scale[ari]['ages'] + ' years old.')