import requests
import json

while True:
    page = 1
    keyword = input('enter a keyword to search for quotes:  ')
    keyword = keyword.lower().strip()
    while True:
        headers = {'Authorization': 'Token token=""'}
        params = {'filter': keyword, 'page': page, 'Accept': 'application/json'}
        response = requests.get('https://favqs.com/api/quotes', headers=headers, params=params)
        data = response.json()
        if data['quotes'][0]['body'] == 'No quotes found':
            print('No quotes found')
            break
        print(f'Page: {page}')
        for i in range(len(data['quotes'])):
            print(f'''{data['quotes'][i]['author']}: "{data['quotes'][i]['body']}"''')
        nxt_page = input('Would you like to view the next page? y/n:  ')
        if nxt_page == 'n':
            break
        else:
            page += 1
    replay = input('Would you like to continue searching for quotes? y/n:  ')
    if replay == 'n':
        break
print('Bye Bye')
