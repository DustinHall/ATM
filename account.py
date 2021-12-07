
def show_balance(balance):
    print(balance)
    return balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance += amount
    return balance


def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    return balance


def logout(name):
    print("Goodbye", name, "!")
