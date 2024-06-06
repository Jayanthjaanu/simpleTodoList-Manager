tasks = []

def display_menu():
    """Displays the main menu."""
    print("\nTo-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    """Displays the current tasks."""
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{index}. {task['description']} - {status}")

def add_task():
    """Adds a new task to the list."""
    description = input("Enter the task description: ")
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print("Task added.")

def complete_task():
    """Marks a task as completed."""
    view_tasks()
    task_number = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def remove_task():
    """Removes a task from the list."""
    view_tasks()
    task_number = int(input("Enter the number of the task to remove: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task removed.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the To-Do List Manager."""
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
