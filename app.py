from banking_pkg import account
import random

balance = 0


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("=== Automated Teller Machine ===")
name = input("Enter name to register:")
pin = input("Enter PIN:")
print(name, "has been registered with a starting balance of: $", balance)

while True:
    name_to_validate = input("Enter Name:")
    pin_to_validate = input("Enter PIN:")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid Credentials!")

while True:
    print(atm_menu(name))
    option = input("Choose an option:")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        deposit = account.deposit(balance)
    elif option == "3":
        withdraw = account.withdraw(balance)
        balance = balance - withdraw
        print(balance)
