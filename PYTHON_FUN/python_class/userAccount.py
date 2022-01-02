class BankAccount():
    accounts = []
    def __init__(self, int_rate, balance):
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
        return f"Balance: {self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self



class User:
    def __init__(self, name):
        self.name = name
        # self.amount = 0 #UPDATED
        self.account = {
            "checking" : BankAccount(.02, 0),
            "savings" : BankAccount(.05, 0)
        }
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Saving Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, amount, user, fromAcct, toAcct):
        self.account[fromAcct].balance -= amount
        user.account[toAcct].balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

mike = User("Mike")

mike.account['checking'].deposit(100).deposit(500).deposit(1500).withdraw(500).yeild_interest()
mike.account['savings'].deposit(100).deposit(500).deposit(1500).withdraw(500).yeild_interest()
mike.display_user_balance()

kendra = User("Kendra")
kendra.account['checking'].deposit(100).deposit(800).deposit(1900).withdraw(1500).yeild_interest()
kendra.account['savings'].deposit(300).deposit(500).deposit(1500).withdraw(800).yeild_interest()
kendra.display_user_balance()
kendra.transfer_money(400, mike, "checking", "savings")
mike.transfer_money(800, kendra, "savings", "checking")