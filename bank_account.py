import random

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []  # Stores a summary of all transactions

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited PKR {amount:.2f}")
            print(f"PKR {amount:.2f} deposited successfully! New balance: PKR {self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds available.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        else:
            if self.verify_otp():
                self.balance -= amount
                self.transactions.append(f"Withdrew PKR {amount:.2f}")
                print(f"PKR {amount:.2f} withdrawn successfully! New balance: PKR {self.balance:.2f}")

    def transfer(self, amount, target_account):
        if amount > self.balance:
            print("Insufficient funds available.")
        elif amount <= 0:
            print("Invalid transfer amount. Please enter a positive amount.")
        else:
            if self.verify_otp():
                self.balance -= amount
                target_account.balance += amount
                self.transactions.append(f"Transferred PKR {amount:.2f} to {target_account.name}")
                print(f"PKR {amount:.2f} transferred successfully! New balance: PKR {self.balance:.2f}")

    def verify_otp(self):
        otp = str(random.randint(100000, 999999))
        print(f"OTP for verification: {otp}")
        user_otp = input("Enter the OTP: ")
        if user_otp == otp:
            print("OTP verified successfully.")
            return True
        else:
            print("Invalid OTP. Transaction cancelled.")
            return False

    def check_balance(self):
        print(f"Current balance: PKR {self.balance:.2f}")

    def account_summary(self):
        print(f"\n--- Account Summary for {self.name} ---")
        print(f"Current Balance: PKR {self.balance:.2f}")
        print("Transaction History:")
        if self.transactions:
            for idx, transaction in enumerate(self.transactions, start=1):
                print(f"{idx}. {transaction}")
        else:
            print("No transactions yet.")

def create_account():
    name = input("Enter your name: ")
    while True:
        try:
            initial_balance = float(input("Enter initial deposit amount (PKR): "))
            if initial_balance >= 0:
                break
            else:
                print("Initial deposit cannot be negative. Please try again.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    return BankAccount(name, initial_balance)

def main():
    print("Welcome to the Bank!")
    account = create_account()

    while True:
        print("\nWhat transaction would you like to perform?")
        print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Check Balance\n5. Account Summary\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit (PKR): "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw (PKR): "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "3":
            target_name = input("Enter recipient's name: ")
            target_account = BankAccount(target_name)  # Simulate another account
            try:
                amount = float(input("Enter amount to transfer (PKR): "))
                account.transfer(amount, target_account)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "4":
            account.check_balance()
        elif choice == "5":
            account.account_summary()
        elif choice == "6":
            print("Thank you for banking with us! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
