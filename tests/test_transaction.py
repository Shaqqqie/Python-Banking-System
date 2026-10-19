import unittest
from dataclasses import FrozenInstanceError

from transaction import Transaction


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(500, "deposit", "Money deposited")

    def test_valid_transaction(self):
        self.assertEqual(self.transaction.amount, 500)
        self.assertEqual(self.transaction.transaction_type, "deposit")
        self.assertEqual(self.transaction.description, "Money deposited")

    def test_default_description(self):
        transaction = Transaction(300, "deposit")
        self.assertEqual(transaction.description, "")

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            Transaction(-500, "deposit")

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            Transaction(0, "deposit")

    def test_invalid_transaction_type(self):
        with self.assertRaises(ValueError):
            Transaction(500, "transfer")

    def test_describe(self):
        self.assertEqual(self.transaction.describe(), "deposit: $500 (Money deposited)")

    def test_immutable_transaction(self):
        with self.assertRaises(FrozenInstanceError):
            self.transaction.amount = 1000

        self.assertEqual(self.transaction.amount, 500)