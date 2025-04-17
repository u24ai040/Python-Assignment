# QUESTION 6

class BankAccount:
    
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")

acc_number = input("Enter your account number: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(acc_number, initial_balance)

while True:
        print("\nBank Account Operations:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account Details")
        print("4. Exit")

        choice = input("Choose an option 1 to 4 : ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
