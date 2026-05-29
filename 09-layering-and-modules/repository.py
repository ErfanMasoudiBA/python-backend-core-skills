from abc import ABC, abstractmethod

from exceptions import AccountNotFoundError
from models import BankAccount


class IAccountRepository(ABC):
    @abstractmethod
    def save(self, account: BankAccount) -> None:
        pass

    @abstractmethod
    def get(self, owner: str) -> BankAccount:
        pass


class AccountRepository(IAccountRepository):
    def __init__(self) -> None:
        self._db = dict()

    def save(self, account: BankAccount) -> None:
        self._db[account.owner] = account
        print(f"User {account.owner} added successfully")
        print(self._db)

    def get(self, owner: str) -> BankAccount:
        if owner in self._db:
            return self._db[owner]
        raise AccountNotFoundError("There is no such owner")
