from datetime import datetime
from department import dep_input, dep_search, date_of_birth_input, date_joined_input
from department import phone_input, wage_input, last_name_input, first_name_input
import random
import os
import camelcase

employee_first_name = []
employee_last_name = []
id_number = []
dob = []
date_joined = []
address = []
phone = []
salary = []
department = []

c = camelcase.CamelCase()

filename = "employee_info.txt"
dep_file = "department.txt"

def new_employee_info():
    try:
        first_name=c.hump(first_name_input())
        last_name = c.hump(last_name_input())
        new_id = id_gen()
        date_of_birth=date_of_birth_input()

        if (first_name, last_name, date_of_birth) in zip(employee_first_name, employee_last_name, dob):
            print("This employee already exists in the database.")
            return
        joined = date_joined_input()
        addr_input = input("Please enter address: ")
        addr = c.hump(addr_input)
        phone_number= phone_input()
        wage= wage_input()
        dep = dep_input()

        with open(filename, 'a') as file:
            info = (first_name, last_name,new_id, date_of_birth, joined,addr, phone_number,wage,dep)
            file.write(','.join(map(str, info)) + '\n')

        print("Employee information added successfully.")
    except ValueError:
        print("Error: Invalid input. Please enter the correct format.")
    finally:
        return

def id_gen():
    while True:
        random_number = random.randint(0, 999999)
        new_id = '818' + '{:06d}'.format(random_number)
        if new_id not in id_number:
            id_number.append(new_id)
            return new_id

#new_employee_info()
