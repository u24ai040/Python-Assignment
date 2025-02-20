class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def current_Password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None  

    def New_Password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True 
        return False  

    def is_correct(self, password):
        
        if password == self.current_Password():
            return True
        return False


Password = Password_manager()
while True:
    print("\nMenu:")
    print("1. Set new password")
    print("2. Get Your current password")
    print("3. Check Your password")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_password = input("Enter a new password: ")
        Password.New_Password(new_password)
    elif choice == '2':
        print("Your Current password is:", Password.current_Password())
    elif choice == '3':
        check_password = input("Enter your current password to check: ")
        if Password.is_correct(check_password):
            print("Password is correct.")
        else:
            print("Incorrect password.")
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")


