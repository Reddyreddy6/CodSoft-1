import pickle

# Load tasks from file
def load_tasks(filename="tasks.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except EOFError:
        return []

# Save tasks to file
def save_tasks(tasks, filename="tasks.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(tasks, file)

# Display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{idx + 1}. {task['task']} - {status}")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
