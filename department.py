from datetime import datetime, timedelta
import re
dep_file = "department.txt"

def first_name_input():
    while True:
        first_name = input("Please enter first name: ")
        if re.match("^[A-Za-z\s]+$", first_name):
            return first_name
        else:
            print("Error: Invalid input. First name should only contain letters and spaces.")

def last_name_input():
    while True:
        last_name = input("Please enter last name: ")
        if re.match("^[A-Za-z\s]+$", last_name):
            return last_name
        else:
            print("Error: Invalid input. Last name should only contain letters and spaces.")

def dep_search(dep_input):
    with open(dep_file, "r") as file:
        for line in file:
            if dep_input in line:
                matrix = line.strip().strip("[]").split(", ")
                dep = matrix[0]
                print(f"In department {matrix[1]}")
                return dep  # Return department if found

    return False
def dep_input():
    while True:
        dep_input = input("Enter department number: ")
        dep = dep_search(dep_input)
        if dep == False:
            print("Department not found. Please try again.")
        else:
            return dep
def date_of_birth_input():
    while True:
        date_of_birth = input("Please enter date of birth in MMDDYYYY format: ")
        try:
            dob = datetime.strptime(date_of_birth, "%m%d%Y")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            if age < 16:
                print("Error: Date of birth should indicate a person older than 16 years.")
                continue
            elif dob < datetime(1950, 1, 1):
                print("Error: Date of birth cannot be older than 01/01/1950.")
                continue
            break

        except ValueError:
            print("Error: Invalid date format. Please enter a valid date.")
    return date_of_birth

def date_joined_input():
    while True:
        joined = input("Please enter date joined in MMDDYYYY format: ")
        try:
            date_joined = datetime.strptime(joined, "%m%d%Y")
            current_date = datetime.now()
            future_date_limit = current_date + timedelta(days=365 * 2)  # Two years in the future

            if date_joined < datetime(2020, 1, 1):
                print("Error: Date joined cannot be before than 01/01/2020.")
                continue
            elif date_joined > future_date_limit:
                print("Error: Date joined cannot be more than two years in the future.")
                continue
            break
        except ValueError:
            print("Error: Invalid date format. Please enter a valid date.")
    return joined
def phone_input():
    while True:
        phone_number = input("Please enter a 10-digit phone number: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Error: Invalid phone number. Please enter a 10-digit number.")
    return phone_number

def wage_input():
    while True:
        try:
            wage = float(input("Please enter salary: "))
            formatted_wage = "{:.2f}".format(wage)
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
    return formatted_wage



#recieve command from http api in jason format
#flask package