class Bank:
    def __init__(self):
        self._accounts = {}


    def add_account(self, account_number, account):
        if account_number in self._accounts:
            raise ValueError("Account number already exists")

        self._accounts[account_number] = account


    def get_account(self, account_number):
        return self._accounts[account_number]


    def remove_account(self, account_number):
        if account_number not in self._accounts:
            raise KeyError("Account does not exist")

        del self._accounts[account_number]

        
    def list_accounts(self):
        return list(self._accounts.values())


    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self._accounts:
            raise KeyError("Source does not exist")

        if to_account_number not in self._accounts:
            raise KeyError("Destination does not exist")

        if from_account_number == to_account_number:
            raise ValueError("Cannot transfer to the same account")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        source = self.get_account(from_account_number)
        destination = self.get_account(to_account_number)
        if source.balance < amount:
            raise ValueError("Source account has insufficient funds")

        source.withdraw(amount)
        destination.deposit(amount)


    def total_balance(self):
        return sum(
            account.balance
            for account in self._accounts.values()
        )


    def print_summary(self):
        print("===== Bank Account Summary =====")

        for account_number, account in self._accounts.items():
            print(f"Account {account_number}: {account.owner} | ${account.balance}")

        print(f"Total accounts: {len(self._accounts)}")
        print(f"Total balance: ${self.total_balance()}")

