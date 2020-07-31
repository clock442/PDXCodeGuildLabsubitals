# Convert the input string into a list of ints
card_number = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
card_number_list = card_number.split(' ')
for num in range(len(card_number_list)):
    card_number_list[num] = int(card_number_list[num])


#print(card_number_list)

# Slice off the last digit. That is the check digit.
check_digit = card_number_list.pop(len(card_number_list)-1)
#print(check_digit)

# Reverse the digits.
card_number_list.reverse()
#print(card_number_list)

# Double every other element in the reversed list.
for i in range(0, len(card_number_list), 2):
    card_number_list[i] *= 2
    # Subtract nine from numbers over nine.
    if card_number_list[i] > 9:
        card_number_list[i] -= 9
# print(card_number_list)

# Sum all values.
total = sum(card_number_list)
#print(total)

# Take the second digit of that sum.
total = str(total)
second_digit = total[1]

# If that matches the check digit, the whole card number is valid.
check_digit = str(check_digit)
if check_digit == second_digit:
    print('Valid')
else:
    print('Card not valid.')

