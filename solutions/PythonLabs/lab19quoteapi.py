import requests
import json

# Begin repl
while True:
    # defining a starting page and asking for a keyword that will always be lowercase and have no whitespace on either side
    page = 1
    keyword = input('enter a keyword to search for quotes:  ')
    keyword = keyword.lower().strip()

    # second while loop to allow user to continue to view more pages of that keyword
    while True:

        # access token that was given
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

        # setting parameters, filter by keyword, recieve only json 
        params = {'filter': keyword, 'page': page}  #'Accept': 'application/json'

        # send request to url with header and parameters
        response = requests.get('https://favqs.com/api/quotes', headers=headers, params=params)

        # split data into json style
        data = response.json()

        # if no results found
        if data['quotes'][0]['body'] == 'No quotes found':
            print('No quotes found')
            break

        # keep track of page number
        print(f'Page: {page}')

        # print all quotes on page, ['quotes'] contains all of the data, [i] is the index of the dictionary for an individual quote, ['body'] contains the text for the quote
        for i in range(len(data['quotes'])):
            print(f'''{data['quotes'][i]['author']}: "{data['quotes'][i]['body']}"''')
        
        # allows user to continue in outer while loop which prints the next page
        nxt_page = input('Would you like to view the next page? y/n:  ')

        # allows exit out of outer while loop
        if nxt_page == 'n':
            break
        # if not exiting, replaces page number with the next page
        else:
            page += 1
    # implementation of repl
    replay = input('Would you like to continue searching for quotes? y/n:  ')
    if replay == 'n':
        break
print('Bye Bye')

# Dwight Schrute: "I love catching people in the act. That's why I always whip open doors."