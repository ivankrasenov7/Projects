tasks = []

def add_task():
    task = input("Enter a task: ").strip().lower()
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def mark_task_complete():
    view_tasks()
    task_number = int(input("Enter a specific task number to mark it as complete: "))
    if task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task marked as complete")
    else:
        print("No task was found")

def save_task_to_file():
    file_name = input("Enter the filename to save tasks: ")
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved to file")

def show_menu():
    print("\n---- To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Save Task to a File")
    print("5. Exit")

while True:
    show_menu()
    choice = int(input("Enter a number: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        mark_task_complete()
    elif choice == 4:
        save_task_to_file()
    elif choice == 5:
        print("Goodbye")
        break
    else:
        print("Invalid choice")
