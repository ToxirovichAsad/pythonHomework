import json
import csv

TASKS_FILE = "tasks.json"
CSV_FILE = "tasks.csv"

def load_tasks():
    """Load tasks from tasks.json."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not load tasks.")
        return []

def save_tasks(tasks):
    """Save tasks back to tasks.json."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    print("\nTasks List:")
    print(f"{'ID':<5} {'Task':<20} {'Completed':<10} {'Priority':<8}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<8}")

def calculate_stats(tasks):
    """Calculate and display task statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(task["completed"] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_to_csv(tasks):
    """Convert JSON data to CSV format."""
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks saved to {CSV_FILE}")

if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks)
