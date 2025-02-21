import os

FILE_NAME = "employees.txt"

def ensure_file_exists():
    """Creates the file if it does not exist. got it from interenet"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass  # Create an empty file

   


def add_employee():
    """Adds a new employee record to the file."""
    while True:
        emp_id = input("Enter Employee ID: ").strip()
        if not emp_id.isdigit():
            print("Employee ID must be a number!")
            continue

        # Check for duplicate Employee ID
        with open(FILE_NAME, "r") as file:
            if any(line.startswith(emp_id + ",") for line in file):
                print("Employee ID already exists! Use a unique ID.")
                return

        name = input("Enter Employee Name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Name must only contain letters!")
            continue

        position = input("Enter Employee Position: ").strip()

        salary = input("Enter Employee Salary: ").strip()
        try:
            salary = float(salary)
            if salary < 0:
                print("Salary cannot be negative!")
                continue
        except ValueError:
            print("Invalid salary! Must be a number.")
            continue

        # Ensure the previous record ends with a newline
        with open(FILE_NAME, "a+") as file:
            file.seek(0, os.SEEK_END)  # Move to end of file
            if file.tell() > 0:  # Check if file is not empty
                file.write("\n")  # Add a newline before appending

            file.write(f"{emp_id}, {name}, {position}, {salary}\n")

        print("Employee successfully added!")
        remove_empty_lines()
        break


def view_all_employees():
    """Displays all employee records."""
    with open(FILE_NAME, "r") as file:
        employees = file.readlines()

    if not employees:
        print("No employee records found.")
    else:
        print("\nAll Employees:")
        for emp in employees:
            print(emp.strip())

def search_employee():
    """Searches for an employee by Employee ID."""
    emp_id = input("Enter Employee ID to search: ").strip()
    
    with open(FILE_NAME, "r") as file:
        for line in file:  
            if line.startswith(emp_id + ","):
                print("\nEmployee Found:")
                print(line.strip())
                return
    
    print("Employee not found!")

def update_employee():
    """Updates an employee's details (except Employee ID)."""
    emp_id = input("Enter Employee ID to update: ").strip()
    found = False

    with open(FILE_NAME, "r") as file, open("temp.txt", "w") as temp_file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True
                old_data = line.strip().split(",") 
                old_data = [field.strip() for field in old_data]  # Trim spaces
                
                if len(old_data) < 4:  # Ensuring expected data format
                    print(f"Error: Corrupt data for Employee ID {emp_id}. Skipping update.")
                    temp_file.write(line)
                    continue  

                print(f"\nUpdating Employee: {line.strip()}")

                # Get new inputs (default to old values if empty)
                new_name = input(f"Enter new Name ({old_data[1]}): ").strip() or old_data[1]
                new_position = input(f"Enter new Position ({old_data[2]}): ").strip() or old_data[2]
                new_salary = input(f"Enter new Salary ({old_data[3]}): ").strip() or old_data[3]

                # Validate salary
                try:
                    new_salary = float(new_salary)
                    if new_salary < 0:
                        raise ValueError("Salary cannot be negative!")
                except ValueError:
                    print("Invalid salary! Salary must be a positive number.")
                    temp_file.write(line)  # Keep old data
                    continue  

                temp_file.write(f"{emp_id}, {new_name}, {new_position}, {new_salary}\n")
                print("Employee successfully updated!")
            else:
                temp_file.write(line)  # Keep other records

    if not found:
        print("Employee ID not found!")

    os.replace("temp.txt", FILE_NAME)

def delete_employee():
    """Deletes an employee record based on Employee ID."""
    emp_id = input("Enter Employee ID to delete: ").strip()
    found = False

    with open(FILE_NAME, "r") as file, open("temp.txt", "w") as temp_file:
        for line in file:
            if line.startswith(emp_id + ","):
                found = True  
                continue  
            temp_file.write(line)

    if not found:
        print("Employee ID not found!")
        return

    os.replace("temp.txt", FILE_NAME)  # Replace file with updated version
    print("Employee successfully deleted!")

def remove_empty_lines():
    """Removes empty lines from the employees file."""
    with open(FILE_NAME, "r") as file:
        lines = [line for line in file if line.strip()]  # Keep only non-empty lines

    with open(FILE_NAME, "w") as file:
        file.writelines(lines)

def main_menu():
    """Displays the main menu and handles user choices."""
    ensure_file_exists()

    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main_menu()
