from abc import ABC, abstractmethod

from database import get_db_connection
from exceptions import AccountNotFoundError
from models import BankAccount


class IAccountRepository(ABC):
    @abstractmethod
    def save(self, account: BankAccount) -> None:
        pass

    @abstractmethod
    def get(self, owner: str) -> BankAccount:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass


# class AccountRepository(IAccountRepository):
#     def __init__(self) -> None:
#         self._db = dict()

#     def save(self, account: BankAccount) -> None:
#         self._db[account.owner] = account
#         print(f"User {account.owner} added successfully")
#         print(self._db)

#     def get(self, owner: str) -> BankAccount:
#         if owner in self._db:
#             return self._db[owner]
#         raise AccountNotFoundError("There is no such owner")


class SQLiteAccountRepository(IAccountRepository):
    def save(self, account):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """ --begin-sql
                INSERT OR REPLACE INTO accounts (owner, balance) VALUES (?,?)
                --end-sql""",
                (account.owner, account.balance),
            )

    def get(self, owner):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """ --begin-sql
                SELECT balance FROM accounts WHERE owner = ?
                --end-sql""",
                (owner,),
            )
            balance = cursor.fetchone()
            if balance is not None:
                return BankAccount(owner, balance[0])
            raise AccountNotFoundError(f"account for {owner} not found.")

    def get_all(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """ --begin-sql
                SELECT owner, balance from accounts
                --end-sql"""
            )
            rows = cursor.fetchall()
            return [BankAccount(owner, balance) for owner, balance in rows]
