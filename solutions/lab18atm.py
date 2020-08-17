
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def balance_(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance > amount:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        return self.balance * 0.1












atm = ATM(0) # create an instance of our class
print('Welcome to the ATM')
transactions = []
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance_() # call the balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        transactions.append(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
            transactions.append(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'history':
        print(transactions,)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('history  - view transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')