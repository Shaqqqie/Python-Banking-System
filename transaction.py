from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    amount: float
    transaction_type: str
    description: str = ""


    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Transaction amount must be greater than zero")
        if self.transaction_type not in {"deposit", "withdrawal"}:
            raise ValueError("Transaction type can only be deposit or withdrawal")


    def describe(self):
        if not self.description:
            return f"{self.transaction_type}: ${self.amount}"

        return f"{self.transaction_type}: ${self.amount} ({self.description})"



