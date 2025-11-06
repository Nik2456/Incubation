class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print("Account Balance=",account.get_balance())
account.deposit(500)
print("Account Balance=",account.get_balance())
