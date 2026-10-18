
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        print("Savings Account Deposit")
        super().deposit(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        super().deposit(interest)
        print("Interest Added:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            print("Current Account Withdrawal")
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                extra = amount - self.get_balance()
                super().withdraw(self.get_balance())
                print("Overdraft Used:", extra)
        else:
            print("Overdraft limit exceeded")


# Create accounts
savings = SavingsAccount("Nikhil", 5000, 5)
current = CurrentAccount("Rahul", 3000, 2000)

# Polymorphism
accounts = [savings, current]

for account in accounts:
    account.display()
    account.deposit(1000)
    account.withdraw(2000)
    print("Final Balance:", account.get_balance())
    print()

savings.add_interest()
print("Savings Balance After Interest:", savings.get_balance())
