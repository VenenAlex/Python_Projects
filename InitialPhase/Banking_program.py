### Banking Program
import time
def show_balance(balance):
    print(f"Your balance is ${balance:,.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited : "))
    if amount <= 0 :
        print("Invalid amount, Deposit an amount which is greater than $0")
        return 0
    else :
        print(f"Depositing ${amount:,.2f}, please wait")
        time.sleep(2)
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : "))
    if amount > balance:
        print("Insufficient funds!!")
        return 0
    elif amount <= 0:
        print("Invalid amount!!")
        return 0
    else:
        print(f"Withdrawing ${amount:,.2f}, please wait")
        time.sleep(2)
        return amount



balance = 0
is_running = True
while is_running:
    print("*"*60)
    print("Banking Program".center(60," "))
    print("*"*60)
    print()
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print()
    print("*"*60)
    choice = int(input("Enter your choice (1-4) : "))
    if choice == 1:
        show_balance(balance)
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw(balance)
    elif choice == 4:
        is_running = False
    else:
        print("*"*60)
        print("Invalid Option!!!")
        print("*"*60)
        print()
print()
print("*"*60)
print("Thank You, Have a nice day!")
print("*"*60)