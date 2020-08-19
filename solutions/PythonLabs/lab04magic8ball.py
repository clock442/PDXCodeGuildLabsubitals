import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 
'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 
'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 
'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 
'Very doubtful']

x = True
while x:
    input('Ask me a question.')
    print(random.choice(answers))
    y = input('Would you like to play again?: y/n')
    if y == 'n':
        x = False