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




# Web Scraper using BeautifulSoup and Requests:
# This Python code snippet scrapes data from a website using the BeautifulSoup library to parse HTML and the Requests library to fetch web pages.


import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print some data from the webpage
title = soup.title.string
print(f'Title: {title}')

# Find and print all links on the webpage
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
    

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
Object-Oriented Programming (OOP):
An example of a Python class that represents a simple bank account.

    
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds')

    def get_balance(self):
        return self.balance

account1 = BankAccount('12345')
account1.deposit(1000)
account1.withdraw(500)
print(f'Account Balance: {account1.get_balance()}')


# Data Analysis with Pandas:
# An example of using the Pandas library for data analysis.


import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}




# User
# give me example DSA questions and solutions code in  python language
# ChatGPT
# Certainly! Here are some example data structures and algorithms (DSA) questions along with Python solutions:

# 1. Reverse a String:
# Write a Python function to reverse a string.

def reverse_string(s):
    return s[::-1]

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)


# 2. Find the Maximum Element in an Array:
# Write a Python function to find the maximum element in an array.


def find_max_element(arr):
    if len(arr) == 0:
        return None
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example usage
numbers = [5, 3, 9, 1, 7]
max_num = find_max_element(numbers)
print(f"The maximum element is {max_num}")


# 3. Check for Palindrome:
# Write a Python function to check if a given string is a palindrome.


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage
test_str = "A man a plan a canal Panama"
is_palindrome_result = is_palindrome(test_str)
print(f'Is it a palindrome? {is_palindrome_result}')

# 4. Implement Binary Search:
# Write a Python function to perform binary search on a sorted array.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result_index = binary_search(sorted_array, target_value)
print(f"Element {target_value} found at index {result_index}")


# 5. Implement a Linked List:
# Create a simple singly linked list in Python with basic operations like insertion and deletion.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()



#6 Binary Search on a List of Strings:

def binary_search_strings(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

string_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "mango"]
target_string = "fig"
result_index = binary_search_strings(string_list, target_string)
print(f"String '{target_string}' found at index {result_index}")

#7 Binary Search for Floating-Point Numbers:

def binary_search_floats(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

float_list = [0.1, 0.2, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]
target_float = 2.0
result_index = binary_search_floats(float_list, target_float)
print(f"Float {target_float} found at index {result_index}")


#8 Binary Search on a List of Objects (Custom Objects):

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

def binary_search_objects(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].roll == target.roll:
            return mid
        elif arr[mid].roll < target.roll:
            low = mid + 1
        else:
            high = mid - 1
    return -1

student_list = [Student(101, "Alice"), Student(102, "Bob"), Student(103, "Charlie"), Student(104, "David")]
target_student = Student(102, "Bob")
result_index = binary_search_objects(student_list, target_student)
print(f"Student with roll {target_student.roll} found at index {result_index}

# 9
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def check_googly_number(N):
    digit_sum = sum(map(int, str(N)))
    if is_prime(digit_sum):
        return "GOOGLY"
    else:
        return "NOT GOOGLY"

# Input
N = int(stdin.readline().strip())

# Check if the number is GOOGLY
result = check_googly_number(N)

# Output
print(result)


# 10
from sys import stdin

def count_digit_occurrence(number, digit):
    return str(number).count(str(digit))

def find_max_occurrence_element(arr, k):
    max_occurrence = -1
    max_occurrence_element = -1

    for element in arr:
        occurrence = count_digit_occurrence(element, k)
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_occurrence_element = element

    return max_occurrence_element

# Input
te, k = map(int, stdin.readline().strip().split())
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Check if the array is empty
if n == 0:
    print(-1)
else:
    result = find_max_occurrence_element(arr, k)
    # Check if there is no occurrence of digit k in the array
    if result == -1:
        print(-1)
    else:
        print(result)








