tasks = []

def add_task():
    print("\nAdd New Task")
    task = input("Enter task: ")
    tasks.append({'task': task, 'status': 'Pending'})
    print("Task added successfully!")

def view_tasks():
    print("\nTo-Do List")
    if tasks:
        for idx, task in enumerate(tasks):
            print(f"{idx+1}. {task['task']} - {task['status']}")
    else:
        print("No tasks found.")

def update_task():
    print("\nUpdate Task")
    task_number = int(input("Enter task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter new task description: ")
        tasks[task_number]['task'] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def mark_task_as_completed():
    print("\nMark Task as Completed")
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['status'] = 'Completed'
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def delete_task():
    print("\nDelete Task")
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_task_as_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
