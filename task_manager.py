import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file, returns an empty list if the file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Saves the task list to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_name):
    """Adds a new task to the task list."""
    tasks = load_tasks()
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task_name}")

def list_tasks():
    """Displays the list of tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\n📋 Task List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['name']} - {status}")

def complete_task(task_number):
    """Marks a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✅ Task '{tasks[task_number - 1]['name']}' marked as completed.")
    else:
        print("⚠️ Invalid task number.")

def delete_task(task_number):
    """Deletes a task from the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed_task['name']}' deleted.")
    else:
        print("⚠️ Invalid task number.")
