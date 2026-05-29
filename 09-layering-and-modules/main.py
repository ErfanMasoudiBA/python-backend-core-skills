from repository import AccountRepository
from service import check_money_account, create_account, transfer_money


def main() -> None:
    central_repo = AccountRepository()
    create_account(central_repo, "Ali", 2000)
    create_account(central_repo, "Negin", 1800)

    print("Negin: ", check_money_account(central_repo, "Negin"))
    print("Ali: ", check_money_account(central_repo, "Ali"))

    transfer_money(repo=central_repo, from_owner="Alii", to_owner="Negin", amount=330)
    print("Negin: ", check_money_account(central_repo, "Negin"))
    print("Ali: ", check_money_account(central_repo, "Ali"))
    pass


main()
