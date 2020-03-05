class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        """add the amount to the balance and return the new balance"""
        self.balance += amount
        return self.balance

    def debit(self, amount):
        """ If the amount is less than the balance,
        reduce the balance by the amount and return the new balance.
        Otherwise return 'Amount exceeded balance' """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return 'Amount exceeded balance'

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
