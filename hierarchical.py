class  BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("deposited ",amount)
    def withdraw(self,amount): 
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("withdraw:", amount)
        else:
            print("low balance")
    def display_balance(self):
        print("the balance in your account is:", self.balance)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance,interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("interest",interest,"is added")
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"withdraw ₹{amount} using overdraft")
        else:
            print("overdraft limit exceeded")

savings = SavingsAccount("Vinay",15000, 10)
savings.deposit(1000)
savings.display_balance()
savings.add_interest()
savings.display_balance()
savings.withdraw(5000)
savings.display_balance()

