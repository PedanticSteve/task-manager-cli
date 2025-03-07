import task_manager

def main():
    while True:
        print("\n📌 Task Manager CLI")
        print("1️⃣ Add a Task")
        print("2️⃣ List Tasks")
        print("3️⃣ Complete a Task")
        print("4️⃣ Delete a Task")
        print("5️⃣ Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_manager.list_tasks()
            task_number = int(input("Enter task number to complete: "))
            task_manager.complete_task(task_number)
        elif choice == "4":
            task_manager.list_tasks()
            task_number = int(input("Enter task number to delete: "))
            task_manager.delete_task(task_number)
        elif choice == "5":
            print("👋 Exiting Task Manager. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
