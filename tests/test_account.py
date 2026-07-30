import pytest
from src.account import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(1, 100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_decreases_balance():
    account = BankAccount(1, 100)
    account.withdraw(30)
    assert account.balance == 70

def test_equality_same_id():
    b1 = BankAccount(1, 100)
    b2 = BankAccount(1, 200)
    assert b1 == b2