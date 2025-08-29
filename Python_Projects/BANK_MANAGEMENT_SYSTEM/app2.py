import datetime

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.record_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.record_transaction("WITHDRAW", amount)
        else:
            print("Insufficient balance!")

    def record_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("Python_Projects/BANK_MANAGEMENT_SYSTEM/statements.txt", "a") as f:
            f.write(f"{self.account_number},{transaction_type},{amount},{timestamp}\n")

    def __str__(self):
        return f"Account({self.account_number}) - {self.name}, Balance: {self.balance}"


class Bank:
    ACCOUNT_FILE = "Python_Projects/BANK_MANAGEMENT_SYSTEM/accounts.txt"

    def __init__(self):
        self.accounts = self.load_accounts()
        self.next_account_number = self.get_next_account_number()

    def load_accounts(self):
        accounts = {}
        try:
            with open(self.ACCOUNT_FILE, "r") as f:
                for line in f:
                    account_number, name, balance = line.strip().split(",")
                    accounts[account_number] = Account(account_number, name, float(balance))
        except FileNotFoundError:
            pass
        return accounts

    def save_accounts(self):
        with open(self.ACCOUNT_FILE, "w") as f:
            for acc in self.accounts.values():
                f.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def get_next_account_number(self):
        if self.accounts:
            return max(int(acc) for acc in self.accounts.keys()) + 1
        return 1001  # starting account number

    def create_account(self, name, initial_balance=0):
        account_number = str(self.next_account_number)
        account = Account(account_number, name, initial_balance)
        self.accounts[account_number] = account
        self.next_account_number += 1
        self.save_accounts()
        print(f"Account created successfully! Account Number: {account_number}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            self.save_accounts()
            print("Deposit successful!")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            self.save_accounts()
            print("Withdrawal successful!")
        else:
            print("Account not found!")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print("Account not found!")

    def view_statement(self, account_number):
        try:
            with open("Python_Projects/BANK_MANAGEMENT_SYSTEM/statements.txt", "r") as f:
                print(f"\n--- Statement for Account {account_number} ---")
                found = False
                for line in f:
                    acc_no, txn_type, amount, timestamp = line.strip().split(",")
                    if acc_no == account_number:
                        print(f"{timestamp} | {txn_type} | ₹{amount}")
                        found = True
                if not found:
                    print("No transactions found.")
        except FileNotFoundError:
            print("No transactions recorded yet.")


def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Statement")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(name, balance)

        elif choice == "2":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_no, amount)

        elif choice == "3":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_no, amount)

        elif choice == "4":
            acc_no = input("Enter account number: ")
            bank.check_balance(acc_no)

        elif choice == "5":
            acc_no = input("Enter account number: ")
            bank.view_statement(acc_no)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
