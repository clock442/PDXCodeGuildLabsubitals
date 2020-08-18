import requests
import json

# response = requests.get('https://favqs.com/api/qotd')

# data = response.json()
# print(f'''{data['quote']['author']}: "{data['quote']['body']}"''')
while True:
    keyword = input('enter a keyword to search for quotes:  ')
    page = int(input('What page do you want:  '))
    # if page != int:
    #     print('not a number')
    #     continue
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    params = {'filter': keyword, 'page': page, 'Accept': 'application/json'}
    response = requests.get('https://favqs.com/api/quotes', headers=headers, params=params)
    data = response.json()
    # elif page > len(data['quotes']):
    #     print('not enough pages, pick a lower number')

    # print(data)
    for i in range(len(data['quotes'])):
        print(f'''{data['quotes'][i]['author']}: "{data['quotes'][i]['body']}"''')
