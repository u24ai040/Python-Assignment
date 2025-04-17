# QUESTION 3

class Bank:
    def __init__(self):
        self.accounts = {}  

    def create_account(self, account_number, name, initial_balance):
        if account_number in self.accounts:
            print("Account number already exists! Try again.")
        else:
            self.accounts[account_number] = {"name": name, "balance": initial_balance}
            print(f"Account for {name} created successfully!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Account not found!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def display_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"\nAccount Number: {account_number}")
            print(f"Name: {account['name']}")
            print(f"Balance: ₹{account['balance']}")
        else:
            print("Account not found!")


bank = Bank()

while True:
        print("\nBanking System:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Choose an option from 1 to 5 : ")

        if choice == '1':
            acc_no = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial deposit amount: "))
            bank.create_account(acc_no, name, initial_balance)

        elif choice == '2':
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_no, amount)

        elif choice == '3':
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_no, amount)

        elif choice == '4':
            acc_no = input("Enter account number: ")
            bank.display_account(acc_no)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
