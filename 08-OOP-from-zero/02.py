class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.validate_init(owner, balance)
        self.owner = owner
        self.balance = balance

    def validate_init(self, owner: str, balance: int) -> None:
        if not isinstance(owner, str):
            raise TypeError("owner is not str")
        if not isinstance(balance, int):
            raise TypeError("balance is not int")

    def validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount is must be more than zero")

    def validate_withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("There is not enough amount")

    def deposit(self, amount: int) -> None:
        self.validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.validate_amount(amount)
        self.validate_withdraw(amount)
        self.balance -= amount


def _test_bank_account_deposit() -> None:

    account1 = BankAccount("ali", 1000)
    account2 = BankAccount("sara", 500)

    # happy paths

    account1.deposit(200)
    assert account1.balance == 1200, "Deposit failed"

    account1.withdraw(700)
    assert account1.balance == 500, "withdraw failed"

    account1.withdraw(500)
    assert account1.balance == 0, "withdraw failed"

    # sad paths

    try:
        account3 = BankAccount(123, 123)
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        account4 = BankAccount("javad", "123")
        assert False, "Expected TypeError"
    except TypeError:
        pass

    try:
        account1.deposit(-200)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        account2.withdraw(-2000)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        account2.withdraw(2000)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    print("All tests passed successfully!")


_test_bank_account_deposit()
