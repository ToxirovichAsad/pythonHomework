import json
import os

class Account:
    """Represents a bank account."""
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ${amount:.2f} from account {self.account_number}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount. Make sure it's a positive number and does not exceed the balance.")
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"

class Bank:
    """Manages multiple bank accounts."""
    FILE_NAME = "accounts.json"
    
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def generate_account_number(self):
        return str(len(self.accounts) + 1001)  # Simple unique ID generator
    
    def create_account(self, name, initial_deposit):
        if not name.strip():
            print("Name cannot be empty.")
            return
        if not isinstance(initial_deposit, (int, float)) or initial_deposit < 0:
            print("Initial deposit must be a non-negative number.")
            return

        account_number = self.generate_account_number()
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump({acc_num: vars(acc) for acc_num, acc in self.accounts.items()}, file)
    
    def load_from_file(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                try:
                    data = json.load(file)
                    self.accounts = {acc_num: Account(**info) for acc_num, info in data.items()}
                except json.JSONDecodeError:
                    print("Error loading account data.")

    def menu(self):
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter your name: ")
                try:
                    initial_deposit = float(input("Enter initial deposit amount: "))
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                    continue
                self.create_account(name, initial_deposit)
            elif choice == "2":
                acc_number = input("Enter account number: ")
                self.view_account(acc_number)
            elif choice == "3":
                acc_number = input("Enter account number: ")
                try:
                    amount = float(input("Enter amount to deposit: "))
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                    continue
                self.deposit(acc_number, amount)
            elif choice == "4":
                acc_number = input("Enter account number: ")
                try:
                    amount = float(input("Enter amount to withdraw: "))
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
                    continue
                self.withdraw(acc_number, amount)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bank = Bank()
    bank.menu()
