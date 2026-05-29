from exceptions import AccountNotFoundError, InsufficientFundsError
from models import BankAccount
from repository import IAccountRepository


def transfer_money(
    repo: IAccountRepository, from_owner: str, to_owner: str, amount: int
) -> bool:
    try:
        from_owner_account = repo.get(from_owner)
        to_owner_account = repo.get(to_owner)
        from_owner_account.withdraw(amount)
        to_owner_account.deposit(amount)
        return True

    except InsufficientFundsError:
        print("There is an error with deposit/withdraw")
        return False
    except AccountNotFoundError:
        print("There is no such a user account")
        return False


def create_account(repo: IAccountRepository, owner: str, amount: int) -> None:
    user_account = BankAccount(owner, amount)
    repo.save(user_account)


def check_money_account(repo: IAccountRepository, owner: str) -> int:
    bank_account_address = repo.get(owner)
    return bank_account_address.balance
