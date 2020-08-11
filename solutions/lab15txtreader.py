import requests
import string
import re

with open('book.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# finding every word in the text and putting it in a list
txt_word_list = re.findall(r"\s?\w+'?\w*\s+", text)
# making all of the words lowercase with no white space
fixed_word_list = []
for word in txt_word_list:
    fixed_word_list.append(word.lower().strip())

# putting all of the words into a dictionary with the word as the key and the count of occurences as the value.
word_dict = {}
for word in fixed_word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] = word_dict[word] + 1
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
