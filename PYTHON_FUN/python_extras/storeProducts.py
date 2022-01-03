class Store:
    products = []
    def __init__(self, name, products):
        self.name = name
        self.products = products
        # self.price = args[0]
        # self.category = args[1]
        Store.products.append(self)
        # self.products = products

    # def __repr__(self):
    #     for i in self.products:
    #         print(f"<__main__.Store: products = " + str(self.products) + ">")

    def print_products(self):
        converted_products = list(self.products)
        # print(converted_products)
        for i in converted_products:
            print(f"<__main__.Store: products = " + str(self.products[0]) + ">")

    def add_product(self, new_product):
        self.new_product = new_product
        self.products.append(new_product)

    def sell_product(self, id):
        self.id = id
        for i in self.products:
            if i == self.id:
                self.products.remove(self.id)

    def inflation(self, percent_increase):
        self.percent_increase = percent_increase
        self.price += self.percent_increase * self.price

    def set_clearance(self, category, percent_discount):
        self.percent_discount
        pass
        #  - updates all the products matching the given category by reducing the price 
        #  by the percent_discount given (use the method you wrote in the Product class!)


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        # self.product = Store(self.name, self.price, self.category)

    def update_price(self, percent_changed, is_increased):
        self.perecent_changed = percent_changed
        self.is_increased
        if is_increased == True:
            self.price += self.percent_changed * self.price
        else:
            self.price -= self.percent_changed * self.price
        print(self.name, self.products, self.price)

    def print_info(self):
        print(f"Product Name: {self.name}, Product Price: {self.price}, Product Category: {self.category}")

###################################################################################
###################################################################################
############################# TEST TEST TEST ######################################
###################################################################################
###################################################################################
###################################################################################
class BankAccount():
    accounts = []
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        # self.amount = 0 #UPDATED
        self.account = BankAccount(self.name, self.int_rate, self.balance)

# mike = User("Mike", .1, 1000)
# print(mike.name)
# print(f"{mike.account.name}'s current balance: {mike.account.balance}")
# print(mike.account.int_rate)

# kendra = User("Kendra", .12, 2000)
# print(kendra.name)
# print(f"{kendra.account.name}'s current balance: {kendra.account.balance}")
# print(kendra.account.int_rate)


###################################################################################
###################################################################################
###################################################################################
###################################################################################
broccoli = Product("Broccoli", 3.50, "Vegetable")
print(broccoli.print_info())
bacon = Product("Bacon", 5.50, "Meat")

generalStore = Store("Mikes General Store", broccoli)
generalStore = Store("Mikes General Store", bacon)
print(generalStore.products.category)
print(generalStore.products.price)

# generalStore = Store("Mike's General Store", ["Cookies", "Bubble Gum", "Broccoli"])
# print(generalStore.name)
# print(generalStore.products[0])

# broccoli = Product("Broccoli", "3.50", "Vegetable")
# print(broccoli.print_info())
# generalStore.add_product("Bacon")
# print(generalStore.products)
# generalStore.sell_product("Bacon")
# print(generalStore.products)
# broccoli.inflation(.15)
# print(generalStore.products[2].price)
