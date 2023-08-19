print("Hello world")

# ////////////////////////////////////////


num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is positive.")

for i in range(1, 6):
    print(f"Square of {i} is {i ** 2}")

# ////////////////////////////////////////



fruits = ["apple", "banana", "cherry", "date"]

print("Original list:", fruits)

fruits.append("grape")
fruits.insert(1, "kiwi")
fruits.remove("cherry")

print("Modified list:", fruits)

for fruit in fruits:
    print(fruit.upper())

sorted_fruits = sorted(fruits)
print("Sorted list:", sorted_fruits)


# ////////////////////////////////////////

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

# Main program
def main():
    print("Welcome to the Banking System!")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(account_number, account_holder, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display_balance()
        elif choice == 4:
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
