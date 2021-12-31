class User:
    # CONSTRUCTOR FUNCTION -- CREATES AN INSTANCE OF AN OBJECT
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = 0

    def greeting(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}. Nice to meet you! I am {self.age} years old!")

    def make_deposit(self, amount):
        print(f"I am making a deposit in the amount of {amount}. Woo hoo!")
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        print(f"I am making a withdrawal in the amount of {amount}.")
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"The current balance is {self.account_balance}")

    def transfer_money(self, user1, user2, amount):
        print(f"{user1.upper()}'s account balance is {mike.account_balance}")
        print(f"{user2.upper()}'s account balance is {kendra.account_balance}")
        print(f"{user1.upper()} is transferring {amount} to {user2.upper()}")
        mike.account_balance -= amount
        kendra.account_balance += amount
        # print(mike.account_balance)
        # print(user1.account_balance)

        # user2.account_balance += amount
        print(f"{user1.upper()}'s account balance is now {mike.account_balance}")
        print(f"{user2.upper()}'s account balance is now {kendra.account_balance}")


mike = User("Mike", "Magruder", 50)
kendra = User("Kendra", "Thayer", 49)
jason = User("Jason", "Peacock", 50)

mike.make_deposit(5000)
mike.make_deposit(5000)
mike.make_deposit(5000)
mike.make_withdrawal(1000)
mike.display_user_balance()

kendra.make_deposit(10000)
kendra.make_deposit(10000)
kendra.make_withdrawal(15000)
kendra.make_withdrawal(10)
kendra.display_user_balance()

kendra.make_deposit(10000)
kendra.make_withdrawal(100)
kendra.make_withdrawal(300)
kendra.make_withdrawal(1800)
kendra.display_user_balance()

mike.transfer_money("mike", "kendra", 1000)

#################################################################################
################ THIS IS THE INSTRUCTOR'S SOLUTION.##############################
#################################################################################

class User2:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


adrien = User2("Adrien")
nibbles = User2("Mr. Nibbles")
benny_bob = User2("Benny Bob")

adrien.make_deposit(100)
adrien.make_deposit(200)
adrien.make_deposit(50)
adrien.make_withdrawl(45)
adrien.display_user_balance()

nibbles.make_deposit(1000)
nibbles.make_deposit(1000)
nibbles.make_withdrawl(500)
nibbles.make_withdrawl(300)
nibbles.display_user_balance()

benny_bob.make_deposit(1500)
benny_bob.make_withdrawl(1000)
benny_bob.make_withdrawl(5000)
benny_bob.make_withdrawl(3000)
benny_bob.display_user_balance()


nibbles.transfer_money(400, adrien)