from dataclasses import FrozenInstanceError

from transaction import Transaction


class BankAccount:
    bank_name = "Python National Bank"
    interest_rate = 0.03
    
    def __init__(self, owner, balance=0):
        self.owner = owner

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = balance

        self.transactions = []


    def __str__(self):
        return f"Bank account belongs to {self.owner}, with a balance of ${self._balance}."


    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance!r})"


    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return(
            self.owner == other.owner
            and self._balance == other._balance
        )

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        transaction = Transaction(amount, "deposit", "Money deposited")
        self.transactions.append(transaction)
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        transaction = Transaction(amount, "withdrawal", "Money withdrawn")
        self.transactions.append(transaction)
        self._balance -= amount


    @property
    def balance(self):
        return self._balance


    def get_transactions(self):
        return self.transactions.copy()


