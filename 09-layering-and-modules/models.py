from exceptions import InsufficientFundsError


class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self._validate_init(owner, balance)
        self.owner = owner
        self._balance = balance

    def _validate_init(self, owner: str, balance: int) -> None:
        if not isinstance(owner, str):
            raise TypeError("owner is not str")
        if not isinstance(balance, int):
            raise TypeError("balance is not int")

    def _validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount is must be more than zero")

    def _validate_withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise InsufficientFundsError("There is not enough amount")

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        self._validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        self._validate_withdraw(amount)
        self._balance -= amount
