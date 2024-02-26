def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks added yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

def mark_task_done(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task index!")

def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
