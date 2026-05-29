class BankAccountError(Exception):
    pass


class InsufficientFundsError(BankAccountError):
    pass


class AccountNotFoundError(BankAccountError):
    pass
