import random
from datetime import date


class Bank:
    Savings_account = {}
    Current_account = {}
    accounts = []
    balance = 0
    loan_amount = 0
    loan_available = True
    loan_list = ['Type 1 : Home Loan Amount : 10k With 6 Months Installment 5% Interest',
                 'Type 2: Car Loan Amount : 20k With 6 Months Installment 5% Interest', 'Car Loan Amount :']
    loan_money = {0: 10000, 1: 20000}
    loan = {0: 'Home Loan', 1: 'Car Loan'}
    account_number_list = []
    acc_no_to_acc = {}

    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_account(self, user, account_no):
        if user in self.accounts:
            print('User already registered')
            return -2
        if user.account_type == 'Current':
            if account_no in self.Current_account:
                print('Already Exist, Try Again')
                return -1
            else:
                self.Current_account[account_no] = user
                print(f'Current Account Created, Designation : {self.Current_account[account_no].designation}, Account Number : {account_no}')
                self.accounts.append(user)
                self.account_number_list.append(account_no)
                self.acc_no_to_acc[account_no] = user
                return account_no
        else:
            if user.account_type == 'Savings':
                if account_no in self.Savings_account:
                    print('Already Exist, Try Again')
                    return -1
                else:
                    self.Savings_account[account_no] = user
                    print(f'Savings Account Created, Designation : {self.Savings_account[account_no].designation}, Account Number : {account_no}')
                    self.accounts.append(user)
                    self.account_number_list.append(account_no)
                    self.acc_no_to_acc[account_no] = user
                    return account_no

    @staticmethod
    def withdraw(self, user, amount):
        if self.balance < amount:
            print('Bank is bankrupt')
            return
        if user in self.accounts:
            if user.account_no in self.Savings_account:
                if self.Savings_account[user.account_no].balance < amount:
                    print('Withdrawal amount exceeded')
                else:
                    self.Savings_account[user.account_no].balance -= amount
                    user.transactions.append(f'Withdraw amount {amount} on {date.today()}')
                    self.balance -= amount
                    print('Withdrawal Successful')
            else:
                if self.Current_account[user.account_no].balance < amount:
                    print('Withdrawal amount exceeded')
                else:
                    self.Current_account[user.account_no].balance -= amount
                    user.transactions.append(f'Withdraw amount {amount} on {date.today()}')
                    self.balance -= amount
                    print('Withdrawal Successful')
        else:
            print('Account does not exist')

    @staticmethod
    def loan_request(self, user):
        if not self.loan_available:
            print('No Loan Services available right now !')
            return
        if user in self.accounts:
            if len(user.loan) >= 2:
                print('Sorry you cannot take more than two loans')
            else:
                print(f'You can take any of them {self.loan_list}')
        else:
            print('Account does not exist')

    @staticmethod
    def taking_loan(self, user, loan_type):
        loan_type -= 1
        if self.balance < self.loan_money[loan_type]:
            self.loan_available = False
        if user in self.accounts:
            if len(user.loan) >= 2:
                print('Loan Limit Exceeded')
            elif not self.loan_available:
                print('This Services is not available right now !')
            else:
                print('Loan taking successful')
                val = (self.loan_list[loan_type], self.loan_money[loan_type])
                user.loan.append(val)
                user.transactions.append(f'Yo you take our loan {self.loan[loan_type] if loan_type == 0 else self.loan[loan_type]} on {date.today()}')
                self.loan_amount += self.loan_money[loan_type]
                self.balance -= self.loan_money[loan_type]
        else:
            print('Account does not exist')

    @staticmethod
    def deposit(self, user, amount):
        if user in self.accounts:
            if user.account_no in self.Savings_account:
                self.Savings_account[user.account_no].balance += amount
                self.balance += amount
                user.transactions.append(f'Deposit amount {amount} on {date.today()}')
                print('Deposit Successful')
            else:
                self.Current_account[user.account_no].balance += amount
                user.transactions.append(f'Deposit amount {amount} on {date.today()}')
                self.balance += amount
                print('Deposit Successful')
        else:
            print('Account does not exist')

    @staticmethod
    def loan_on_of(self):
        self.loan_available ^= True
        if self.loan_available:
            print('Loan activated successfully')
        else:
            print('Loan deactivated successfully')

    @staticmethod
    def check_balance(self):
        return self.balance

    @staticmethod
    def check_total_loan(self):
        return self.loan_amount

    @staticmethod
    def del_user(self, user):
        if user in self.accounts:
            for i in range(len(user.loan)):
                self.balance += user.loan[i][1]
                self.loan_amount -= user.loan[i][1]
            self.account_number_list.remove(user.account_no)
            self.balance -= user.balance
            del self.acc_no_to_acc[user.account_no]
            self.accounts.remove(user)
            if user.account_no in self.Savings_account:
                del self.Savings_account[user.account_no]
            else:
                del self.Current_account[user.account_no]
            print('Deleting User: ', user.account_no)
            user.balance = 0
            user.transactions.clear()
            user.loan.clear()
            user = None
            del user
        else:
            print('Account does not exist')

    @staticmethod
    def transfer(self, user, acc_no, amount):
        if user.balance < amount:
            print('Not enough money')
            return
        if acc_no not in self.account_number_list:
            print('Account does not exist')
            return
        t_user = self.acc_no_to_acc[acc_no]
        user.balance -= amount
        user.transactions.append(f'You transfer {amount} to account number : {t_user.account_no}')
        print('Transfer Money Successfully')
        if t_user.account_no in self.Savings_account:
            self.Savings_account[t_user.account_no].balance += amount
            self.Savings_account[t_user.account_no].transactions.append(f'You received {amount} from  {self.Savings_account[user.account_no].name} on {date.today()}')
        else:
            self.Current_account[t_user.account_no].balance += amount
            self.Current_account[t_user.account_no].transactions.append(f'You received {amount} from  {self.Current_account[user.account_no].name} on {date.today()}')

    @staticmethod
    def user_list(self, user):
        for i in self.accounts:
            print(f'Name : {i.name}, Email : {i.email}, Balance : {i.balance}, Loans : {i.loan}, Account Number : {i.account_no}')


def create_account(self, account_no):
    return Bank.create_account(Bank, self, account_no)


def withdraw_money(self, amount):
    Bank.withdraw(Bank, self, amount)


def deposit_money(self, amount):
    Bank.deposit(Bank, self, amount)


def loan_request(self):
    Bank.loan_request(Bank, self)


def transfer(self, user, account, amount):
    Bank.transfer(Bank, user, account, amount)


class User:
    def __init__(self, name, email, phone, address, account_type, designation):
        self.account_no = None
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = list(tuple())
        self.transactions = []
        self.designation = designation

    def create_account(self):
        while True:
            acc = random.randint(10000000, 1000000000)
            yo = create_account(self, acc)
            if yo == -2:
                break
            if yo == acc:
                self.account_no = acc
                break

    def withdraw(self, amount):
        withdraw_money(self, amount)

    def deposit(self, amount):
        deposit_money(self, amount)

    def check_balance(self):
        print('Balance: ', self.balance)

    def transactions_history(self):
        print(f'{self.name} Transactions History :')
        cnt = 1
        for tx in self.transactions:
            print('Transaction ', cnt, ': ', tx)
            cnt += 1

    def take_loan(self):
        loan_request(self)

    def taking_loan(self, loan_type):
        Bank.taking_loan(Bank, self, loan_type)

    def transfer_money(self, user, account_number, amount):
        Bank.transfer(Bank, user, account_number, amount)


class Admin(User):
    def __init__(self, name, email, phone, address, account_type, designation):
        super().__init__(name, email, phone, address, account_type, designation)

    def self_account(self):
        while True:
            acc = random.randint(10000000, 1000000000);
            yo = create_account(self, acc)
            if yo == -2:
                break
            if yo == acc:
                self.account_no = acc
                break

    def info_account(self, user):
        while True:
            acc = random.randint(10000000, 1000000000)
            yo = create_account(user, acc)
            if yo == -2:
                break
            if yo == acc:
                user.account_no = acc
                break

    def del_account(self, user):
        Bank.del_user(Bank, user)

    def user_list(self):
        Bank.user_list(Bank, self)

    def loan_system_toggle(self):
        Bank.loan_on_of(Bank)

    def check_bank_balance(self):
        print('Bank Balance : ', Bank.check_balance(Bank))

    def check_loan_amount(self):
        print('Bank Loan : ',Bank.check_total_loan(Bank))


rainy = User('Rainy', 'rainy@gmail.com', '01718XXXXXX', 'Uttor Badda', 'Current', 'Tester')
rocky = User('Rocky', 'rocky@gmail.com', '01914XXXXXX', 'East Nakhalpara', 'Savings', 'Student')
robin = User('Robin', 'robin@gmail.com', '01514XXXXXX', 'Uttara', 'Savings', 'Student')
admin = Admin('Md. Rakibul Hasan', 'heisenberg@gmail.com', '01608XXXXXX', 'Tejgaon', 'Current', 'Manager')
admin.create_account()


def services():
    while True:
        print('Enter 1 : Creating Account\n'
              'Enter 2 : Deposit Money\n'
              'Enter 3 : Withdraw Money\n'
              'Enter 4 : Check Balance\n'
              'Enter 5 : Check Transactions History\n'
              'Enter 6 : Loan Services\n'
              'Enter 7 : Transfer Money\n'
              'Enter 8 : Creating Account By Admin\n'
              'Enter 9 : Exit\n')
        inp = input('Enter your choice : ')
        if inp == '1':
            username = input('Enter your username : ')
            if username == 'rainy':
                rainy.create_account()
            elif username == 'rocky':
                rocky.create_account()
            elif username == 'robin':
                robin.create_account()
            else:
                print('Invalid Username')
        elif inp == '2':
            username = input('Enter your username : ')
            if username == 'rainy':
                amount = int(input('Enter your amount : '))
                rainy.deposit(amount)
            elif username == 'rocky':
                amount = int(input('Enter your amount : '))
                rocky.deposit(amount)
            elif username == 'robin':
                amount = int(input('Enter your amount : '))
                robin.deposit(amount)
            else:
                print('Invalid Username')
        elif inp == '3':
            username = input('Enter your username : ')
            if username == 'rainy':
                amount = int(input('Enter your amount : '))
                rainy.withdraw(amount)
            elif username == 'rocky':
                amount = int(input('Enter your amount : '))
                rocky.withdraw(amount)
            elif username == 'robin':
                amount = int(input('Enter your amount : '))
                robin.withdraw(amount)
            else:
                print('Invalid Username')
        elif inp == '4':
            username = input('Enter your username : ')
            if username == 'rainy':
                rainy.check_balance()
            elif username == 'rocky':
                rocky.check_balance()
            elif username == 'robin':
                robin.check_balance()
            else:
                print('Invalid Username')
        elif inp == '5':
            username = input('Enter your username : ')
            if username == 'rainy':
                rainy.transactions_history()
            elif username == 'rocky':
                rocky.transactions_history()
            elif username == 'robin':
                robin.transactions_history()
            else:
                print('Invalid Username')
        elif inp == '6':
            print('Welcome to Our Bank Loan ')
            name = input('Enter your username : ')
            if name == 'rainy' or name == 'rocky' or name == 'robin':
                print('Type 1 : See all loan available or Type 2 : For taking loans')
                typ = input('Enter your choice : ')
                if typ == '1':
                    if name == 'rainy':
                        rainy.take_loan()
                    elif name == 'rocky':
                        rocky.take_loan()
                    elif name == 'robin':
                        robin.take_loan()
                    else:
                        print('Invalid Username')
                else:
                    if name == 'rainy':
                        print('Which Type of loan you would like to : ')
                        tp = int(input('Enter your choice : '))
                        rainy.taking_loan(tp)
                    elif name == 'rocky':
                        print('Which Type of loan you would like to : ')
                        tp = input('Enter your choice : ')
                        rocky.taking_loan(tp)
                    elif name == 'robin':
                        print('Which Type of loan you would like to : ')
                        tp = input('Enter your choice : ')
                        robin.taking_loan(tp)
                    else:
                        print('Invalid Username')

            else:
                print('Invalid Username')

        elif inp == '7':
            print('Enter your bank username then account number on which you want to transfer money and also amount : ')
            username = input('Enter your username : ')
            account_number, amount = map(int, input('Account Number and Amount : ').split())
            if username == 'rainy':
                rainy.transfer_money(rainy, account_number, amount)
            elif username == 'rocky':
                rocky.transfer_money(rocky, account_number, amount)
            elif username == 'robin':
                robin.transfer_money(robin, account_number, amount)
            else:
                print('Invalid Username')
        elif inp == '8':
            print('Please Provide a valid username')
            username = input('Enter your username : ')
            if username == 'rainy':
                admin.info_account(rainy)
            elif username == 'rocky':
                admin.info_account(rocky)
            elif username == 'robin':
                admin.info_account(robin)
            else:
                print('Invalid Username')
        else:
            break


while True:
    print('There is an admin account for admin with username : admin who is the manager of the bank\n'
          'Three user accounts available with username : rainy, rocky and robin these are not open account\n'
          'But if he want he can open by himself or admin can create it too\n')
    typ = input('Enter 1 if you user or 2 if you admin or 3 for exit : ')
    if typ == '1':
        services()
    elif typ == '2':
           username = input('Enter your username : ')
           if username == 'admin':
               while True:
                   print('Enter 1 : Creating Account By Admin with provide username of an users\n'
                         'Enter 2 : Delete Account with provide username of an users\n'
                         'Enter 3 : All Account List of the Bank\n'
                         'Enter 4 : Check Total Available Bank Balance\n'
                         'Enter 5 : Check Total Loan Amount\n'
                         'Enter 6 : Toggle the Loaning System\n'
                         'Enter 7 : exit')
                   inp = input('Enter your choice : ')
                   if inp == '1':
                       print('Please Provide a valid username')
                       username = input('Enter your username : ')
                       if username == 'rainy':
                           admin.info_account(rainy)
                       elif username == 'rocky':
                           admin.info_account(rocky)
                       elif username == 'robin':
                           admin.info_account(robin)
                       else:
                           print('Invalid Username')
                   elif inp == '2':
                       print('Please Provide a valid username')
                       username = input('Enter your username : ')
                       if username == 'rainy':
                           admin.del_account(rainy)
                       elif username == 'rocky':
                           admin.del_account(rocky)
                       elif username == 'robin':
                           admin.del_account(robin)
                       else:
                           print('Invalid Username\n')
                   elif inp == '3':
                       admin.user_list()
                   elif inp == '4':
                       admin.check_bank_balance()
                   elif inp == '5':
                       admin.check_loan_amount()
                   elif inp == '6':
                       admin.loan_system_toggle()
                   else:
                       break
           else:
               print('Invalid Username\n')
    else:
        break













