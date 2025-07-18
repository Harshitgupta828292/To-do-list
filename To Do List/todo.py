tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
      
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added successfully.")

def remove_tasks():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        save_tasks()
        print(f"Task '{removed_task}' removed successfully.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Here is your to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    load_tasks() 
    while True:
        print("\nOPTIONS: 1. Add Task  2. Remove Task  3. Show Tasks  4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_tasks()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("Exiting to-do list.")
            break
        else:
            print("Invalid choice. Try again!")

main()
