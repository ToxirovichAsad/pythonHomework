import csv
import os
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class CSVStorage:
    FILE_NAME = "tasks.csv"

    @staticmethod
    def save_tasks(tasks):
        with open(CSVStorage.FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
    
    @staticmethod
    def load_tasks():
        tasks = []
        if os.path.exists(CSVStorage.FILE_NAME):
            with open(CSVStorage.FILE_NAME, "r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if row:
                        tasks.append(Task(*row))
        return tasks

class TaskManager:
    def __init__(self):
        self.tasks = CSVStorage.load_tasks()
    
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_status(self, status):
        return status in ["Progress", "Completed"]
    
    def add_task(self):
        while True:
            task_id = input("Enter Task ID: ")
            if not task_id.isdigit():
                print("Error: Task ID must be a number!")
                continue
            if any(task.task_id == task_id for task in self.tasks):
                print("Error: Task ID already exists!")
                continue
            break
        
        title = input("Enter Title: ").strip()
        if not title:
            print("Error: Title cannot be empty!")
            return
        
        description = input("Enter Description: ").strip()
        
        while True:
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            if self.validate_date(due_date):
                break
            print("Error: Invalid date format! Use YYYY-MM-DD.")
        
        while True:
            status = input("Enter Status (Progress/Completed): ")
            if self.validate_status(status):
                break
            print("Error: Invalid status! Choose from Progress, or Completed.")
        
        self.tasks.append(Task(task_id, title, description, due_date, status))
        CSVStorage.save_tasks(self.tasks)
        print("Task added successfully!\n")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)
            print()
    
    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ").strip()
                if not task.title:
                    print("Error: Title cannot be empty!")
                    return
                
                task.description = input("Enter new Description: ").strip()
                
                while True:
                    due_date = input("Enter new Due Date (YYYY-MM-DD): ")
                    if self.validate_date(due_date):
                        task.due_date = due_date
                        break
                    print("Error: Invalid date format!")
                
                while True:
                    status = input("Enter new Status (Progress/Completed): ")
                    if self.validate_status(status):
                        task.status = status
                        break
                    print("Error: Invalid status!")
                
                CSVStorage.save_tasks(self.tasks)
                print("Task updated successfully!\n")
                return
        print("Error: Task not found.\n")
    
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        CSVStorage.save_tasks(self.tasks)
        print("Task deleted successfully!\n")
    
    def filter_tasks(self):
        while True:
            status = input("Enter status to filter (In Progress/Completed): ")
            if self.validate_status(status):
                break
            print("Error: Invalid status!")
        
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with this status.\n")
        else:
            print("Filtered Tasks:")
            for task in filtered_tasks:
                print(task)
            print()
    
    def menu(self):
        while True:
            print("Welcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                CSVStorage.save_tasks(self.tasks)
                print("Tasks saved successfully!\n")
            elif choice == "7":
                self.tasks = CSVStorage.load_tasks()
                print("Tasks loaded successfully!\n")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = TaskManager()
    manager.menu()
