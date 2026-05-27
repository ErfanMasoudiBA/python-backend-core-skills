class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance = self.balance + amount


account1 = BankAccount("ali", 1000)
account2 = BankAccount("sara", 500)

account1.deposit(200)

print(account1.balance)
print(account2.balance)
