class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0.0
        self.menu()
    
    def menu(self):
        while True:
            user_input = int(input("""
                           Press 1 to Create PIN
                           Press 2 to Check Balance
                           Press 3 to Withdraw
                           Press 4 to Deposit
                           Press 5 to Change PIN
                           Press 6 to Exit\n"""))
            if user_input == 1:
                self.pin_creation()
            elif user_input == 2:
                self.check_balance()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.deposit()
            elif user_input == 5:
                self.change_pin()
            elif user_input == 6:
                print("Thank you for using our service!")
                break
            else:
                print("Invalid option. Please try again.\n")
    
    def pin_creation(self):
        pin = input("Enter your new PIN (4 digits):\n")
        con_pin = input("Enter your PIN again to confirm:\n")
        if pin.isdigit() and len(pin) == 4 and pin == con_pin:
            self.pin = pin
            self.balance = float(input("Enter your initial balance:\n"))
            print("PIN successfully created.\n")
        else:
            print("PIN creation failed. Ensure your PIN is numeric and matches the confirmation.\n")
        self.menu()
    
    def check_balance(self):
        pin = input("Enter your PIN:\n")
        if pin == self.pin:
            print(f"Your account balance is: {self.balance:.2f}\n")
        else:
            print("Incorrect PIN.\n")
        self.menu()
    
    def withdraw(self):
        pin = input("Enter your PIN:\n")
        if pin == self.pin:
            amount = float(input("Enter the amount to withdraw:\n"))
            if amount > self.balance:
                print("Insufficient funds.\n")
            else:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is: {self.balance:.2f}\n")
        else:
            print("Incorrect PIN.\n")
        self.menu()
    
    def deposit(self):
        pin = input("Enter your PIN:\n")
        if pin == self.pin:
            amount = float(input("Enter the amount to deposit:\n"))
            self.balance += amount
            print(f"Deposit successful. Your new balance is: {self.balance:.2f}\n")
        else:
            print("Incorrect PIN.\n")
        self.menu()
    
    def change_pin(self):
        pin = input("Enter your current PIN:\n")
        if pin == self.pin:
            new_pin = input("Enter your new PIN (4 digits):\n")
            con_new_pin = input("Enter your new PIN again to confirm:\n")
            if new_pin.isdigit() and len(new_pin) == 4 and new_pin == con_new_pin:
                self.pin = new_pin
                print("PIN successfully updated.\n")
            else:
                print("PIN update failed. Ensure your new PIN is numeric and matches the confirmation.\n")
        else:
            print("Incorrect current PIN.\n")
        self.menu()

# Create an instance of the ATM class
obj = ATM()
