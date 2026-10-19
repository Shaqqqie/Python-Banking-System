from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)

        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = interest_rate


    def __str__(self):
        return f"Savings account belonging to {self.owner} with balance of ${self.balance}"

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest <= 0:
            return None

        self.deposit(interest)

