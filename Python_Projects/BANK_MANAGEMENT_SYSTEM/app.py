class Account:
    def __init__(self, acc_no, name, balance=0.0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New Balance: ₹{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display(self):
        print(f"\nAccount No: {self.acc_no}\nName: {self.name}\nBalance: ₹{self.balance}")


class BankSystem:
    FILE_NAME = "Python_Projects/BANK_MANAGEMENT_SYSTEM/accounts.txt"

    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        accounts = {}
        try:
            with open(self.FILE_NAME, "r") as f:
                for line in f:
                    acc_no, name, balance = line.strip().split(",")
                    accounts[acc_no] = Account(acc_no, name, float(balance))
        except FileNotFoundError:
            with open(self.FILE_NAME, "w") as f:
                pass
        return accounts

    def save_accounts(self):
        with open(self.FILE_NAME, "a") as f:
            for acc in self.accounts.values():
                f.write(f"{acc.acc_no},{acc.name},{acc.balance}\n")

    def generate_account_number(self):
        if not self.accounts:
            return "1001"   # starting account number
        # get the maximum existing account number
        max_acc = max(int(acc_no) for acc_no in self.accounts.keys())
        return str(max_acc + 1)

    def create_account(self, name, balance=0.0):
        acc_no = self.generate_account_number()
        self.accounts[acc_no] = Account(acc_no, name, balance)
        self.save_accounts()
        print(f"Account created successfully! Your Account Number is {acc_no}")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)
            self.save_accounts()
        else:
            print("Account not found.")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)
            self.save_accounts()
        else:
            print("Account not found.")

    def display_account(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].display()
        else:
            print("Account not found.")


def main():
    bank = BankSystem()

    while True:
        print("\n=============== Bank Account Management =================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            bank.create_account(name, balance)

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Deposit: "))
            bank.deposit(acc_no, amount)

        elif choice == "3":
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Withdraw: "))
            bank.withdraw(acc_no, amount)

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            bank.display_account(acc_no)

        elif choice == "5":
            print("============== Thank you for using our Bank System! =================")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
