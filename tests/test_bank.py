import unittest

from bank import Bank
from bank_account import BankAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

        self.alice = BankAccount("Alice", 1000)
        self.bob = BankAccount("Bob", 500)

        self.bank.add_account(1001, self.alice)
        self.bank.add_account(1002, self.bob)

    def test_add_account(self):
        self.bank.add_account(1003, BankAccount("Charlie", 1500))
        
        self.assertEqual(len(self.bank.list_accounts()), 3)

    def test_duplicate_account(self):
        with self.assertRaises(ValueError):
            self.bank.add_account(1001, BankAccount("Charlie", 1200))

        self.assertEqual(len(self.bank.list_accounts()), 2)

    def test_get_account(self):
        self.assertIs(self.bank.get_account(1001), self.alice)

    def test_missing_account(self):
        with self.assertRaises(KeyError):
            self.bank.get_account(1003)

    def test_remove_account(self):
        self.assertEqual(len(self.bank.list_accounts()), 2)

        self.bank.remove_account(1001)

        self.assertEqual(len(self.bank.list_accounts()), 1)
        with self.assertRaises(KeyError):
            self.bank.get_account(1001)

    def test_list_accounts(self):
        list_accounts = self.bank.list_accounts()

        self.assertEqual(list_accounts[0], self.bank.get_account(1001))
        self.assertEqual(list_accounts[1], self.bank.get_account(1002))

    def test_total_balance(self):
        self.assertEqual(self.bank.total_balance(), 1500)

    def test_transfer(self):
        self.bank.transfer(1001, 1002, 200)

        source = self.bank.get_account(1001)
        destination = self.bank.get_account(1002)

        self.assertEqual(source.balance, 800)
        self.assertEqual(destination.balance, 700)

        self.assertEqual(len(source.get_transactions()), 1)
        self.assertEqual(len(destination.get_transactions()), 1)

        source_transaction = source.get_transactions()[0]
        destination_transaction = destination.get_transactions()[0]

        self.assertEqual(source_transaction.amount, 200)
        self.assertEqual(source_transaction.transaction_type, "withdrawal")

        self.assertEqual(destination_transaction.amount, 200)
        self.assertEqual(destination_transaction.transaction_type, "deposit")

    def test_insufficient_funds_transfer(self):
        source = self.bank.get_account(1001)
        destination = self.bank.get_account(1002)

        with self.assertRaises(ValueError):
            self.bank.transfer(1001, 1002, 1500)

        self.assertEqual(source.balance, 1000)
        self.assertEqual(destination.balance, 500)

        self.assertEqual(len(source.get_transactions()), 0)
        self.assertEqual(len(destination.get_transactions()), 0)

    def test_transfer_to_same_account(self):
        source = self.bank.get_account(1001)
        with self.assertRaises(ValueError):
            self.bank.transfer(1001, 1001, 500)

        self.assertEqual(len(source.get_transactions()), 0)


    

