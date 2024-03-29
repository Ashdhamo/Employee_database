from department import dep_input, dep_search, date_of_birth_input, date_joined_input,phone_input, wage_input
import camelcase

filename = "employee_info.txt"
c = camelcase.CamelCase()

def pull_employee_info(filename):
    try:
        employee_name = input("Enter the employee's first name: ").lower()
        with open(filename, 'r') as file:
            lines = file.readlines()
            employee_found = False
            for line_number, line in enumerate(lines, 1):
                employee_data = line.strip().split(',')
                current_first_name = employee_data[0].lower()

                if employee_name == current_first_name:
                    employee_found = True
                    print("Employee Information:")
                    print("First Name:", employee_data[0])
                    print("Last Name:", employee_data[1])
                    print("ID:", employee_data[2])
                    print("DOB:", employee_data[3])
                    print("Date joined:", employee_data[4])
                    print("Address:", employee_data[5])
                    print("Phone number:", employee_data[6])
                    print("Salary:", employee_data[7])
                    dep_num = employee_data[8]
                    dep_search(dep_num)


                    edit_employee = input("Please enter 1 to edit employee, 2 to delete, or press any key to skip editing: ")

                    if edit_employee == "1":
                        edit_employee_info(line_number, lines, filename)

                    elif edit_employee == '2':
                        delete_employee_by_index(line_number, lines, filename)
                        print("Employee information deleted successfully.")

                    else:
                        return

                else:
                    continue

            if not employee_found:
                print(f"No employee with the first name '{employee_name}' found.")
                return

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid option.")

def edit_employee_info(line_number, lines, filename):
    try:
        edit_option = input("Press 1 to change first name,\n 2 to change last name,\n "
                            "3 to change date of birth,\n 4 to change date joined,\n "
                            "5 to change address,\n 6 to change phone number,\n "
                            "7 to change salary,\n 8 to change department.txt.\n Else press any key to skip editing: ")

        if edit_option == '1':
            new_first_name_input = input("Enter the new first name: ")
            new_first_name=c.hump(new_first_name_input)
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[0] = new_first_name
            lines[line_number - 1] = ','.join(employee_data) + '\n'

        elif edit_option == '2':
            new_last_name_input = input("Enter the new last name: ")
            new_last_name = c.hump(new_last_name_input)
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[1] = new_last_name
            lines[line_number - 1] = ','.join(employee_data) + '\n'
#New DOB
        elif edit_option == '3':
            new_last_name_input = input("Enter the new last name: ")
            new_last_name = c.hump(new_last_name_input)
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[3] = new_last_name
            lines[line_number - 1] = ','.join(employee_data) + '\n'
#New Joined Date
        elif edit_option == '4':
            new_joined = date_joined_input()
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[4] = new_joined
            lines[line_number - 1] = ','.join(employee_data) + '\n'
#  New Address
        elif edit_option == '5':
            new_addr_input = input("Enter the new address: ")
            new_addr = c.hump(new_addr_input)
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[5] = new_addr
            lines[line_number - 1] = ','.join(employee_data) + '\n'
#New phone
        elif edit_option == '6':
            new_phone_number = phone_input()
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[6] = new_phone_number
            lines[line_number - 1] = ','.join(employee_data) + '\n'
 #New salary
        elif edit_option == '7':
            new_wage = wage_input()
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[6] = str(new_wage)
            lines[line_number - 1] = ','.join(employee_data) + '\n'

        elif edit_option == '8':
            new_dep = dep_input()
            employee_data = lines[line_number - 1].strip().split(',')
            employee_data[6] = new_dep
            lines[line_number - 1] = ','.join(employee_data) + '\n'


        else:
            print("exiting edit. Going to main menu")
            return

        with open(filename, 'w') as file:
            file.writelines(lines)
            print("Employee information updated successfully.")
            return


    except IndexError:
        print("Error: Index out of range. Please try again.")
    except ValueError:
        print("Error: Invalid input. Please enter the correct format.")

def delete_employee_by_index(index, lines, filename):
    try:
        del lines[index - 1]
        with open(filename, 'w') as file:
            file.writelines(lines)
    except IndexError:
        print("Error: Index out of range. Please try again.")
    except ValueError:
        print("Error: Invalid input. Please enter the correct format.")

#pull_employee_info(filename)