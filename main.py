from bank import Bank
from bank_account import BankAccount
from savings_account import SavingsAccount


def display_menu():
        print(
        "\n===== Python Banking System =====\n"
        "1. Create account\n"
        "2. Deposit\n"
        "3. Withdraw\n"
        "4. Transfer\n"
        "5. View account\n"
        "6. List accounts\n"
        "7. Apply savings interest\n"
        "8. Exit\n"
    )


def create_account(bank):
    print("\n===== Create Account =====")

    try:
        account_number = int(input("Account number: "))
        name = input("Owner's name: ")
        starting_balance = float(input("Starting balance: "))
    except ValueError as error:
        print(error)
        return

    while True:
        print("Acccount type: ")
        print("1. Regular account")
        print("2. Savings account")

        choice = input("Choose account type: ").strip()

        if choice not in {"1", "2"}:
            print("Invalid option. Please try again.")
            continue

        try:
            if choice == "1":
                account = BankAccount(name, starting_balance)
                break
            elif choice == "2":
                interest_rate = float(input("Interest rate (e.g. 0.03): "))
                account = SavingsAccount(name, starting_balance, interest_rate)
                break
        except ValueError as error:
            print(error)
            return

    try:
        bank.add_account(account_number, account)
    except ValueError as error:
        print(f"Unable to create account: {error}")
        return
    
    print(f"Account {account_number} successfully created!")


def deposit_money(bank):
    print("===== Deposit Money =====")

    try:
        account_number = int(input("Account number: "))
        deposit_amount = float(input("Deposit amount: "))

        account = bank.get_account(account_number)
        account.deposit(deposit_amount)

        print(f"Successfully deposited ${deposit_amount}")
        print(f"New balance: ${account.balance}")
    except(ValueError, KeyError) as error:
        print(f"Deposit failed:: {error}")


def withdraw_money(bank):
    print("===== Withdraw Money =====")

    try:
        account_number = int(input("Account number: "))
        withdrawal_amount = float(input("Withdrawal amount: "))

        account = bank.get_account(account_number)
        account.withdraw(withdrawal_amount)

        print(f"Successfully withdrew ${withdrawal_amount}")
        print(f"New balance: ${account.balance}")
    except(ValueError, KeyError) as error:
        print(f"Withdrawal failed: {error}")


def transfer_money(bank):
    print("===== Transfer Money =====")

    try:
        source_account_number = int(input("Source account number: "))
        destination_account_number = int(input("Destination account number: "))
        transfer_amount = float(input("Transfer amount: "))

        bank.transfer(source_account_number, destination_account_number, transfer_amount)

        source = bank.get_account(source_account_number)
        destination = bank.get_account(destination_account_number)

        print(f"Successfully transferred ${transfer_amount}")
        print(f"\nSource account balance: ${source.balance}")
        print(f"Destination account balance: ${destination.balance}")
    except(ValueError, KeyError) as error:
        print(f"Transfer failed: {error}")


def view_account(bank):
    print("===== Account Details =====")

    try:
        account_number = int(input("Account number: "))
        account = bank.get_account(account_number)
        print(f"Owner: {account.owner}")
        print(f"Account type: {type(account).__name__}")
        print(f"Balance: ${account.balance}")

        print("\nTransaction history: ")
        account_transactions = account.get_transactions()
        if not account_transactions:
            print("No transactions yet.")
            return
        else:
            for transaction in account_transactions:
                print(transaction.describe())
    except(ValueError, KeyError) as error:
        print(f"Unable to view account: {error}")


def list_accounts(bank):
    if not bank.list_accounts():
        print("No accounts exist to be displayed.")
        return 
    
    bank.print_summary()


def apply_savings_interest(bank):
    print("===== Savings Interest =====")

    try:
        account_number = int(input("Account number: "))

        account = bank.get_account(account_number)
        if not isinstance(account, SavingsAccount):
            print("Savings interest can only be applied to a Savings account")
            return

        account.apply_interest()
        
        print("Interest successfully applied!")
        print(f"New balance: ${account.balance}")
    except(ValueError, KeyError) as error:
        print(f"Unable to apply interest to account: {error}")

def main():
    bank = Bank()

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("Invalid option. Please try again.")
            continue

        if choice == "1":
            create_account(bank)
        elif choice == "2":
            deposit_money(bank)
        elif choice == "3":
            withdraw_money(bank)
        elif choice == "4":
            transfer_money(bank)
        elif choice == "5":
            view_account(bank)
        elif choice == "6":
            list_accounts(bank)
        elif choice == "7":
            apply_savings_interest(bank)    
        elif choice == "8":
            print("Exiting system...")
            break


if __name__ == "__main__":
    main()