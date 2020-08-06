

# fruits = ['apples', 'bananas', 'pears']
# print(fruits[0]) # apples

# # iterating over the element
# for fruit in fruits:
#     print(fruit)

# # iterating over the indices
# for i in range(len(fruits)):
#     print(i, fruits[i])


# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
# def combine_all(nums):

    # new_list = []
    # for i in range(len(nums)):
    #     for j in nums[i]:
    #         new_list.append(j)
    # return new_list

    # new_list = []
    # for i in range(len(nums)):
    #     for j in range(len(nums[i])):
    #         new_list.append(nums[i][j])
    # return new_list

    # new_list = []
    # for inner_list in nums:
    #     for element in inner_list:
    #         new_list.append(element)
    # return new_list

    # new_list = []
    # for inner_list in nums:
    #     new_list.extend(inner_list)
    # return new_list


# print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]




# Problem 12

# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.

# def fibonacci(n):
    # fibo_list = [1, 1]
    # trailing_var = 1
    # running_var = 1
    # for i in range(n-2):
    #     print(trailing_var, running_var)
    #     add_number = trailing_var + running_var
    #     fibo_list.append(add_number)
    #     trailing_var = running_var
    #     running_var = add_number
    # return fibo_list

#     fibo_list = [1, 1]
#     for i in range(1, n-1):
#         fibo_list.append(fibo_list[i] + fibo_list[i-1])
#     return fibo_list
            

  
# print(fibonacci(8)) # [1, 1, 2, 3, 5, 8, 13, 21]


# Problem 13

# # Write a function that takes n as a parameter and returns n factorial.

# def factorial(n):
#     total = n
#     if n == 0:
#         return 1
#     for i in range(n-1, 1, -1):
#         total *= i
#     return total

# def factorial_list(n):
#     new_list = []
#     for i in range(n+1):
#         new_list.append(factorial(i))
#     return new_list


#                           0! 1! 2! 3!  4!   5!   6!
# print(factorial_list(100)) # [1, 1, 2, 6, 24, 120, 720 ]

# print(factorial(0))
# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))










# Problem 14

# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


# def contains(nums,value):
#     for num in nums:
#         if num == value:
#             return True
#     return False

# def find_unique(nums):
#     #return list(set(nums))

#     newlist = []
#     for i in range(len(nums)):
#         # checking if the element is already in newlist, if it is not, add it
#         if nums[i] not in newlist:
#             newlist.append(nums[i])
#     return newlist


    # newlist = []
    # for i in range(len(nums)):
    #     # checking if the element is already in newlist, if it is not, add it
    #     if not contains(newlist, nums[i]):
    #         newlist.append(nums[i])
    # return newlist

    # newlist = []
    # for i in range(len(nums)):
    #     # checking if the element is already in newlist, if it is not, add it
    #     found = False
    #     for num in newlist:
    #         if num == nums[i]:
    #             found = True
    #     if not found:
    #         newlist.append(nums[i])
    # return newlist



# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# print(find_unique(nums)) # [12, 24, 35, 88, 120, 155]


# x = (25, 10, 5, 1)
# (quarter, dime, nickle, penny) = x
# coins = [25, 10, 5, 1]
# coins = [
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]
# while True:
#     coin_amounts = [0, 0, 0, 0]
#     total_cents = float(input('Enter a dollar amount:   '))*100
#     for i in range(len(coins)):
#         current_value = coins[i][1]
#         if total_cents >= current_value:
#             num_coins = total_cents//current_value
#             coin_amounts[i] += num_coins
#             total_cents -= current_value*num_coins
#     print(f'You would have {int(coin_amounts[0])} quarters, {int(coin_amounts[1])} dimes, {int(coin_amounts[2])} nickels, and {int(coin_amounts[3])} pennies.')
#     repeat = input('Would you like to make more change? y/n:   ')
#     if repeat != 'y':
#         print('Bye Bye')
#         break



# def round_pad_zeroes(num, digits=2):
#     num = str(float(round(num, digits)))
#     num += '0'*(digits-len(num)+1+num.index('.'))
#     return num

# print(round_pad_zeroes(5, 3)) # 5.000
# print(round_pad_zeroes(3.1415963, 3)) # 3.142
# print(round_pad_zeroes(3.1, 5)) # 3.10000






def blackjack_advice(current_total, card_add):
    cards = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    # total = cards[card1] + cards[card2]
    # if total < 17:
    #     return 'Hit'
    # elif 16 < total < 21:
    #     return 'Stay'
    # elif total == 21:
    #     return 'Blackjack!'
    # else:
    #     return 'Already Busted'
    # total = cards[card1] + cards[card2]
    # if total > 21:
    #     if card1 or card2 == 'A':
    #         cards['A'] = 1
    #     else:
    #         return 'Already busted'
    # elif total == 21:
    #     return 'Blackjack!'
    # elif 16 < total < 21:
    #     return 'Stay' 
    # elif total < 17:
    #     return 'Hit'
    # else:
    #     return 'Not Valid'

# while True:
#     print('Welcome to Blackjack Advice!')
#     print('Your card choices will be 1 to 9 and J, Q, K, A for the rest.')
#     card1 = str(input('What is your first card?'))
#     card2 = str(input('What is your second card?'))
#     print(blackjack_advice(card1, card2))
#     repeat = input('Would you like to play again? y/n:   ')
#     if repeat == 'n':
#         print('Bye Bye')
#         break
cards = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }


print('Welcome to Blackjack Advice!')
print('We will start at 0 and you will add cards. I will then tell you if you should hit or stay. Your card choices will be 1 to 9 and J, Q, K, A.')
value_list = []
current_total = 0
while current_total < 22:
    new_card = input('What card are you adding?:   ')
    value_list.append(cards[new_card])
    current_total = sum(value_list)
    print(f'Current total is {current_total}')
    if current_total == 21:
        print('Blackjack!')
        break
    elif 16 < current_total < 21:
        print('Stay')
    elif current_total < 17:
        print('Hit')
    elif current_total > 21:
        if new_card == 'A':
            value_list.remove(11)
            value_list.append(1)
            continue
        elif new_card != 'A':
            print('Bust')
            break
    repeat = input('Would you like to continue? y/n:   ')
    if repeat != 'y':
        break











