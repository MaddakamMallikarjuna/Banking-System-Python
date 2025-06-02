class Account:
    def __init__(self, name, account_no, passcode):
        self.name = name
        self.account_no = account_no
        self.passcode = passcode
        self.__balance = 0  # Private balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Enter a positive amount.")

    def withdraw(self, amount, passcode):
        if passcode == self.passcode:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
            else:
                print("Insufficient funds or invalid amount.")
        else:
            print("Incorrect passcode!")

    def __str__(self):
        return f"Name: {self.name}, Account No: {self.account_no}, Balance: {self.__balance}"


class BankSystem:
    def __init__(self):
        self.accounts = {}  # Stores all accounts

    def add_account(self, name, account_no, passcode):
        if account_no in self.accounts:
            print("Account already exists.")  # Check if account exists
        else:
            self.accounts[account_no] = Account(name, account_no, passcode)  # Add new account
            print("Account created.")

    def deposit(self, account_no, amount):
        self.accounts.get(account_no, print("Account not found.")).deposit(amount)  # Deposit money

    def withdraw(self, account_no, amount, passcode):
        self.accounts.get(account_no, print("Account not found.")).withdraw(amount, passcode)  # Withdraw money


def main():
    bank = BankSystem()  # Initialize bank system

    while True:
        print("\n1. Add Account\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            bank.add_account(input("Name: "), input("Account No: "), input("Passcode: "))  # Add account
        elif choice == "2":
            bank.deposit(input("Account No: "), int(input("Amount: ")))  # Deposit money
        elif choice == "3":
            bank.withdraw(input("Account No: "), int(input("Amount: ")), input("Passcode: "))  # Withdraw money
        elif choice == "4":
            print("Goodbye!")  # Exit program
            break
        else:
            print("Invalid choice. Try again.")  # Invalid option


if __name__ == "__main__":
    main()
