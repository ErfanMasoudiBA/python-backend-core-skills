from exceptions import AccountNotFoundError, InsufficientFundsError
from repository import SQLiteAccountRepository
from service import check_money_account, create_account, transfer_money


def main() -> None:
    central_repo = SQLiteAccountRepository()
    create_account(central_repo, "Ali", 2000)
    create_account(central_repo, "Negin", 1800)

    print("Negin: ", check_money_account(central_repo, "Negin"))
    print("Ali: ", check_money_account(central_repo, "Ali"))

    try:
        transfer_money(
            repo=central_repo, from_owner="Ali", to_owner="Negin", amount=330
        )

    except InsufficientFundsError:
        print("There is an error with deposit/withdraw")
        return
    except AccountNotFoundError:
        print("There is no such a user account")
        return

    print("Negin: ", check_money_account(central_repo, "Negin"))
    print("Ali: ", check_money_account(central_repo, "Ali"))


main()
