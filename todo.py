# todo.py - Simple Console-based To-Do List Application

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the text file."""
    try:
        with open(TASK_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()


def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
