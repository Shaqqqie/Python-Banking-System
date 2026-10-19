# Python Banking System

A command-line banking application built with Python to practice object-oriented programming, modular software design, exception handling, and automated testing.

The application supports multiple bank accounts, deposits, withdrawals, transfers, savings interest, and transaction history tracking.

## Features

- **Account Management**
  - Create regular and savings accounts.
  - Retrieve and remove accounts.
  - View individual account details.
  - Display all registered accounts and their combined balance.
  - Prevent duplicate account numbers.

- **Banking Operations**
  - Deposit and withdraw money.
  - Transfer funds between accounts.
  - Validate transaction amounts and available balances.
  - Apply interest to savings accounts.

- **Transaction History**
  - Record deposits and withdrawals.
  - Store transactions using immutable dataclasses.
  - Display transaction descriptions.
  - Protect transaction history from external modification.

- **Command-Line Interface**
  - Interactive menu for banking operations.
  - Input validation and exception handling.
  - User-friendly error messages.

- **Automated Testing**
  - 30 tests using Python's built-in `unittest` framework.
  - Tests for account operations, savings interest, transaction validation, and bank management.
  - Coverage of invalid inputs and expected failure conditions.

## Project Structure

```text
python-banking-system/
├── bank.py
├── bank_account.py
├── savings_account.py
├── transaction.py
├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_bank.py
│   ├── test_bank_account.py
│   ├── test_savings_account.py
│   └── test_transaction.py
├── .gitignore
└── README.md
```

## Technologies Used

- Python 3
- Python Standard Library
- `unittest` — Automated testing
- `dataclasses` — Structured, immutable transaction records

No third-party dependencies are required.

## Getting Started

### Prerequisites

Install Python 3.

Check your installation:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-banking-system.git
cd python-banking-system
```

Replace `YOUR_USERNAME` with your GitHub username.

### Running the Application

```bash
python3 main.py
```

The application displays the following menu:

```text
===== Python Banking System =====
1. Create account
2. Deposit
3. Withdraw
4. Transfer
5. View account
6. List accounts
7. Apply savings interest
8. Exit
```

Follow the prompts to perform banking operations.

## Example Usage

Create two accounts:

```text
Account 1001: Alice | Balance: $1000
Account 1002: Bob | Balance: $500
```

Transfer $200 from Alice to Bob:

```text
Source account number: 1001
Destination account number: 1002
Transfer amount: 200

Successfully transferred $200
```

Updated balances:

```text
Account 1001: Alice | Balance: $800
Account 1002: Bob | Balance: $700
```

## Running Tests

Run the complete test suite from the project root:

```bash
python3 -m unittest discover -s tests -v
```

Test suites cover:

| Module | Tests |
|---|---:|
| BankAccount | 7 |
| SavingsAccount | 6 |
| Transaction | 7 |
| Bank | 10 |
| **Total** | **30** |

All 30 tests passed during development.

## Software Design

The application uses object-oriented programming principles to separate responsibilities.

### BankAccount

The base class responsible for account balances, deposits, withdrawals, and transaction history.

### SavingsAccount

Inherits from `BankAccount` and introduces interest-rate validation and interest calculations.

### Transaction

An immutable dataclass representing an individual deposit or withdrawal.

### Bank

Manages registered accounts, transfers, account retrieval, and balance summaries.

### CLI

Provides an interactive interface while delegating banking operations to the appropriate classes.

## Limitations

This is an educational project and is not intended for real financial transactions.

Current limitations include:

- Account data is stored in memory and is lost when the application exits.
- Monetary values use floating-point numbers rather than `decimal.Decimal`.
- Transfers validate expected failure conditions but do not provide full transactional atomicity.
- No authentication or persistent database storage.

## Potential Improvements

- Introduce SQLite for persistent account storage.
- Use `decimal.Decimal` for monetary calculations.
- Implement atomic transfers using database transactions.
- Add account authentication.
- Introduce type annotations throughout the codebase.
- Extend the application with a REST API using FastAPI.

## Learning Objectives

This project was developed as part of a Python refresher focused on software engineering fundamentals.

Key concepts practiced:

- Classes and objects
- Inheritance and polymorphism
- Encapsulation and properties
- Composition
- Special methods (`__str__`, `__repr__`, `__eq__`)
- Dataclasses and immutability
- Exception handling
- Modules and imports
- Automated unit testing
- Object identity and reference semantics

## License

This project is intended for educational and portfolio purposes. No license has been specified.