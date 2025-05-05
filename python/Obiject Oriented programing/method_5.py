"""Create a class BankAccount with:

An __init__ method to initialize owner and balance attributes.
A method deposit to add an amount to the balance.
A method withdraw to subtract an amount from the balance (if sufficient funds are available).
A method display_balance to print the current balance.
Test the class by creating an account, depositing money, withdrawing money, and displaying the balance. """

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Instance attribute
        self.balance = balance  # Instance attribute

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    # Method to display balance
    def display_balance(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

# Testing the class
name=input("enter your name")
balance=float(input("enter the amount"))
account = BankAccount(name,balance)  # Initial balance = 100
x=float(input("enter you frist acount  deposite blance"))
y=float(input("enter the with draw amount"))
account.deposit(x)  # Deposits 50
account.withdraw(y)  # Withdraws 30
account.display_balance()  # Displays balance
