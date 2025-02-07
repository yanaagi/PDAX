# PDAX
## Overview
This is a simple banking system implemented in Python, following a layered architecture approach. The system allows for account creation, transactions (deposits and withdrawals), and account statement generation.

## Project Structure
The project is structured into the following layers:

- **Domain Layer**: Defines the core entities (`Account` and `Customer`).
- **Infrastructure Layer**: Handles data storage with `AccountRepository`.
- **Use Case Layer**: Implements business logic through use cases.

## Features
- Create a new account for a customer.
- Perform transactions (deposit and withdraw funds).
- Generate an account statement displaying transaction history and final balance.

## Classes and Responsibilities
### Domain Layer
#### `Account`
- Represents a bank account.
- Stores account details, balance, and transaction history.
- Methods:
  - `deposit(amount)`: Adds money to the account.
  - `withdraw(amount)`: Deducts money from the account if sufficient balance is available.
  - `get_balance()`: Returns the current balance.

#### `Customer`
- Represents a bank customer.
- Stores customer details like name, email, and phone number.

### Infrastructure Layer
#### `AccountRepository`
- Provides in-memory storage for accounts.
- Methods:
  - `save_account(account)`: Saves an account.
  - `find_account_by_id(account_id)`: Retrieves an account by ID.
  - `find_accounts_by_customer_id(customer_id)`: Retrieves accounts for a given customer.

### Use Case Layer
#### `CreateAccountUseCase`
- Creates a new customer and associated bank account.
- Stores customer details temporarily.
- Saves the account in `AccountRepository`.

#### `MakeTransactionUseCase`
- Handles deposits and withdrawals.
- Validates transaction type and account existence.

#### `GenerateAccountStatementUseCase`
- Retrieves an account's transaction history.
- Generates a formatted account statement.

## Running the Project
1. Ensure Python is installed on your system.
2. Save the script in a `.py` file.
3. Run the script using:
   ```sh
   python Banking.py
   ```
4. Expected output:
![image](https://github.com/user-attachments/assets/def45f09-a493-48f9-ae34-5980c8c70241)

   ```

