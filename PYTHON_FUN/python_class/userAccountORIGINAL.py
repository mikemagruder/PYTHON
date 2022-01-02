class BankAccount():
    accounts = []
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"{self.name}'s Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    def transfer_money(self, amount, user):
        self.balance -= amount
        user.account.balance += amount
        self.display_account_info()
        user.account.display_account_info()
        return self



class User:
    def __init__(self, name):
        self.name = name
        # self.amount = 0 #UPDATED
        self.account = BankAccount(self.name, int_rate=0.02, balance=0)

    # def make_deposit(self, amount):
    #     self.amount += amount
    #     return self

    # def make_withdrawal(self, amount):
    #     self.amount -= amount
    #     return self

    # def display_user_balance(self):
    #     print(f"User: {self.name}, Balance: {self.amount}")
    #     return self


mike = User("Mike")
print(mike.name)
print(f"{mike.account.name}'s current balance: {mike.account.balance}")
print(mike.account.int_rate)
mike.account.deposit(400).deposit(200).deposit(300).deposit(500).withdraw(500).display_account_info()

kendra = User("Kendra")
print(kendra.name)
print(f"{kendra.name}'s current balance: {kendra.account.balance}")
print(kendra.account.int_rate)
kendra.account.deposit(200).deposit(2000).deposit(30).deposit(500).withdraw(500).display_account_info()
kendra.account.transfer_money(400, mike)
mike.account.transfer_money(800, kendra)