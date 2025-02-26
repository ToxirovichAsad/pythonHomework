import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'w'):
                pass  # Create an empty file if it doesn't exist

    def add_employee(self, employee):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!\n")
    
    def view_all_employees(self):
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        if not records:
            print("No employee records found.\n")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())
            print()
    
    def search_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        for record in records:
            if record.startswith(employee_id + ","):
                print("Employee Found:")
                print(record.strip())
                return record.strip()
        print("Employee not found.\n")
        return None
    
    def update_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        
        updated_records = []
        found = False
        for record in records:
            if record.startswith(employee_id + ","):
                found = True
                print("Enter new details:")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                updated_records.append(f"{employee_id}, {name}, {position}, {salary}\n")
            else:
                updated_records.append(record)
        
        if found:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee updated successfully!\n")
        else:
            print("Employee not found.\n")
    
    def delete_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        
        updated_records = [record for record in records if not record.startswith(employee_id + ",")]
        
        if len(updated_records) == len(records):
            print("Employee not found.\n")
        else:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee deleted successfully!\n")
    
    def menu(self):
        while True:
            print("Welcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                emp = Employee(employee_id, name, position, salary)
                self.add_employee(emp)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                self.update_employee(employee_id)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
