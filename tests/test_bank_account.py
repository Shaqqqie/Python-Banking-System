import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Alice", 1000)
    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_default_balance(self):
        account = BankAccount("Bob")
        self.assertEqual(account.balance, 0)

    def test_negative_initial_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("Alice", -500)

    def test_deposit(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 1200)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-200)

        self.assertEqual(self.account.balance, 1000)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1200)

        self.assertEqual(self.account.balance, 1000)