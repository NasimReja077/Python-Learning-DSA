# to_do_cli.py

FILE_NAME = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print("✅ Task added successfully!")

def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("📭 No tasks found.")
            else:
                print("\n📌 Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("📭 No tasks file found.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)
            print("🗑️ Task deleted successfully!")
        else:
            print("❌ Invalid task number.")
    except:
        print("❌ Error occurred.")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Exiting program. Bye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()


# https://impacthub-gamma.vercel.app/
# https://fullstack-deployment-z3tl.onrender.com/