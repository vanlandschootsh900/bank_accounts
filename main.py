#Shay VanLandschoot
# 5/6/25
# Three Ways to Modify BankAccount Class Attributes

class bankAccount:

    def __init__(self,holder,bal=0):
        self.holder = holder
        self.bal = bal
        
    def deposit(self, amount):

        if amount >0:
            self.bal= amount + self.bal
            print (f'{self.holder} Deposited {amount} Your Balance Is {self.bal}')
        else:
            print('Invalid deposit amount')

    def withdraw(self, amount):
        if amount > 0 and amount <=self.bal:
            self.bal=amount - self.bal
            print(f'Balance Is {self.bal}')
        else:
            print('Invalid withdrawal amount or insufficient funds!')

    def get_bal(self):
        print(self.bal)

    def display_account_info(self):
        print(f'account holder:{self.holder} your balance is {self.bal}')


shay= bankAccount('shay',123)
print()
bankAccount.display_account_info(shay)
run=True
while run:
    print()
    print('''What would you like to do?
    Deposit = 1
    Withdraw = 2
    Get Balance = 3
    Quit = 4''')
    print()
    users_answer = int(input('Enter here:'))
    print
    if users_answer == 1:
        depo = int(input('''How Much would you like to Deposit
        Enter Here:'''))
        bankAccount.deposit(shay,depo)
        print()
    elif users_answer == 2:
        withdraw = int(input('''How Much would you like to Withdraw'
        Enter Here:'''))
        bankAccount.withdraw(shay,withdraw)
        print()
    elif users_answer == 3:
        bankAccount.get_bal(shay)
        print()
    elif users_answer== 4 :
        run=False
    else:
        print('''Invalid Input please enter
    Deposit = 1
    Withdraw = 2
    Get Balance = 3
    Quit = 4''')
    print()