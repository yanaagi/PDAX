# Domain Layer
class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(("deposit", amount))
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(("withdraw", amount))
        else:
            raise ValueError("Invalid withdrawal amount")

    def get_balance(self):
        return self.balance

class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number


# Infrastructure Layer
class AccountRepository:
    def __init__(self):
        self.accounts = {}

    def save_account(self, account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        return self.accounts.get(account_id, None)

    def find_accounts_by_customer_id(self, customer_id):
        return [acc for acc in self.accounts.values() if acc.customer_id == customer_id]

# Use Case Layer
class CreateAccountUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository
        self.customers = {} 

    def create_account(self, account_id, customer_id, account_number, name, email, phone_number):
        customer = Customer(customer_id, name, email, phone_number)
        self.customers[customer_id] = customer
        account = Account(account_id, customer_id, account_number)
        self.account_repository.save_account(account)
        return account, customer

class MakeTransactionUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")

class GenerateAccountStatementUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")
        statement = f"Account Statement for {account.account_number}\n"
        statement += "Transactions:\n"
        for transaction in account.transactions:
            statement += f"{transaction[0]}: ${transaction[1]}\n"
        statement += f"Final Balance: ${account.get_balance()}\n"
        return statement


class MakeTransactionUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdraw":
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")


class GenerateAccountStatementUseCase:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")
        
        statement = f"Account Statement for {account.account_number}\n"
        statement += "Transactions:\n"
        for transaction in account.transactions:
            statement += f"{transaction[0]}: ${transaction[1]}\n"
        statement += f"Final Balance: ${account.get_balance()}\n"
        return statement


# Test Scenario
if __name__ == "__main__":
    repo = AccountRepository()
    create_account_uc = CreateAccountUseCase(repo)
    transaction_uc = MakeTransactionUseCase(repo)
    statement_uc = GenerateAccountStatementUseCase(repo)

    # Create an account with customer details
    account, customer = create_account_uc.create_account(1, 101, "ACC123", "John Doe", "john@example.com", "1234567890")
    print(f"Created Account: {account.account_number}, Balance: ${account.get_balance()}, Customer: {customer.name}")

    # Perform transactions
    transaction_uc.make_transaction(1, 500, "deposit")
    transaction_uc.make_transaction(1, 200, "withdraw")

    # Generate account statement
    statement = statement_uc.generate_account_statement(1)
    print(statement)
