from add_employee import new_employee_info
from pull_employee import pull_employee_info
import os

filename = "employee_info.txt"
dep_file = "department.txt"

def welcome_page():
    print("Welcome to Ashwini Inc, employee database")
    password = ""
    while password != "Ashwini":
        password = input("Please enter password: ")
        if password != "Ashwini":
            print("Wrong password. Please try again.")

# Lets user choose if they want to add info or find a user
def main_menu():
    while True:
        try:
            choice1 = int(input("To fetch and update employee info, press 1.\nTo add new employee info, press 2. \nTo exit, press 3: "))
            if choice1 == 1:
                pull_employee_info(filename)
            elif choice1 == 2:
                new_employee_info()
            elif choice1 == 3:
                return
        except ValueError:
            print("Error: Invalid input. Please enter a number.")



main_menu()