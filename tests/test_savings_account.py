import unittest

from savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.account = SavingsAccount("Alice", 1000, 0.05)

    def test_default_interest_rate(self):
        account = SavingsAccount("Bob", 1200)
        self.assertEqual(account.interest_rate, 0.03)

    def test_custom_interest_rate(self):
        self.assertEqual(self.account.interest_rate, 0.05)

    def test_negative_interest_rate(self):
        with self.assertRaises(ValueError):
            SavingsAccount("Bob", 1000, -0.05)

    def test_apply_interest(self):
        self.assertEqual(self.account.balance, 1000)

        self.account.apply_interest()

        self.assertEqual(self.account.balance, 1050)
        self.assertEqual(len(self.account.get_transactions()), 1)

        transaction = self.account.get_transactions()[0]

        self.assertEqual(transaction.amount, 50)
        self.assertEqual(transaction.transaction_type, "deposit")

    def test_zero_interest_rate(self):
        account = SavingsAccount("Bob", 1200, 0)

        account.apply_interest()

        self.assertEqual(account.balance, 1200)

    def test_zero_balance_interest(self):
        account = SavingsAccount("Bob", 0, 0.05)

        account.apply_interest()

        self.assertEqual(account.balance, 0)
        