class BankAccount():
    accounts = []
    def __init__(self,int_rate,balance):
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
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

acct1 = BankAccount(.12, 1500)
acct2 = BankAccount(.1, 1000)

savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

acct1.deposit(200).deposit(300).deposit(500).withdraw(500).yeild_interest().display_account_info()
acct2.deposit(20).deposit(50).deposit(120).withdraw(800).yeild_interest().display_account_info()

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

BankAccount.print_all_accounts()