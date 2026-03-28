# ATM Simulation - Basic Version
print("Welcome to ATM System")
pin = 1234
balance = 5000
transactions = 0
# Checking user PIN
pin_input = input("Enter your PIN: ")

if pin_input.isdigit():
    entered_pin = int(pin_input)
else:
    print("Invalid PIN input")
    exit()

if entered_pin == pin:
# ATM Menu Loop (runs until user exits)
    while True:
        print("\n------ ATM MENU ------")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Exit")
# Option 1: Show current balance
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)
# Option 2: Withdraw money from account
        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance = balance - amount
                print("Withdraw successful")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")
# Option 3: Deposit money into account
        elif choice == 3:
            amount = int(input("Enter deposit amount: "))
            balance = balance + amount
            print("Deposit successful")
            print("Updated balance:", balance)
# Option 4: Exit from ATM system
        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")
try:
    choice = int(input("Enter your choice: "))
except:
    print("Enter valid number")
    def show_balance(balance):
     print("Your balance is:", balance)
     def check_balance(balance):
      print("Your balance is:", balance)

def deposit(balance):
    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Invalid deposit amount")
        return balance

    balance = balance + amount
    print("Deposit successful")
    print("Updated balance:", balance)

    return balance
def withdraw(balance):
    amount = int(input("Enter withdrawal amount: "))

    if amount > 2000:
        print("Withdrawal limit is 2000")
        return balance

    if amount <= balance:
        balance = balance - amount
        print("Withdraw successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

    return balance