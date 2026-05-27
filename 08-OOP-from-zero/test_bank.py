import pytest
from bank import BankAccount  # نام فایلی که کلاس در آن است را جایگزین کن


# -----------------------------------------
# ۱. تست‌های ساخت شیء (Initialization)
# -----------------------------------------
def test_create_account_success():
    account = BankAccount("ali", 1000)
    assert account.owner == "ali"
    assert account.balance == 1000


def test_create_account_invalid_owner_type():
    with pytest.raises(TypeError, match="owner is not str"):
        BankAccount(123, 1000)


def test_create_account_invalid_balance_type():
    with pytest.raises(TypeError, match="balance is not int"):
        BankAccount("javad", "123")


# -----------------------------------------
# ۲. تست‌های واریز (Deposit)
# -----------------------------------------
def test_deposit_success():
    account = BankAccount("ali", 1000)
    account.deposit(200)
    assert account.balance == 1200


def test_deposit_negative_amount():
    account = BankAccount("ali", 1000)
    with pytest.raises(ValueError, match="Amount is must be more than zero"):
        account.deposit(-200)


# -----------------------------------------
# ۳. تست‌های برداشت (Withdraw)
# -----------------------------------------
def test_withdraw_success():
    account = BankAccount("ali", 1000)
    account.withdraw(700)
    assert account.balance == 300

    account.withdraw(300)
    assert account.balance == 0


def test_withdraw_negative_amount():
    account = BankAccount("sara", 500)
    with pytest.raises(ValueError, match="Amount is must be more than zero"):
        account.withdraw(-2000)


def test_withdraw_insufficient_funds():
    account = BankAccount("sara", 500)
    with pytest.raises(ValueError, match="There is not enough amount"):
        account.withdraw(2000)


# -----------------------------------------
# ۴. تست کپسوله‌سازی و Read-only بودن (Encapsulation)
# -----------------------------------------
def test_balance_is_readonly():
    account = BankAccount("ali", 1000)
    # تلاش برای تغییر مستقیم موجودی باید مسدود شود
    with pytest.raises(AttributeError):
        account.balance = 2000
