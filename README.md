# ✅ Task Manager CLI

A simple **Python-based Task Manager CLI** that allows users to **add, list, complete, and delete tasks**.  
Tasks are **stored in a JSON file**, ensuring persistence across sessions.

## 🚀 Features
✅ Add new tasks  
✅ List all tasks  
✅ Mark tasks as complete  
✅ Delete tasks  
✅ Data stored in `tasks.json` for persistence  

## 📁 Project Structure
```
task-manager-cli/
│── task_manager.py # Module for task operations
│── main.py # Main CLI script
│── tasks.json # Task storage file
│── README.md # Documentation
```

## 🛠 Installation & Usage
### 🔹 1. Clone the Repository
```
sh
git clone https://github.com/yourusername/task-manager-cli.git
cd task-manager-cli
```
### 🔹 2. Run the Program
```
python main.py
```
### 🔹 3. Use the CLI to Manage Tasks
```
📌 Task Manager CLI
1️⃣ Add a Task
2️⃣ List Tasks
3️⃣ Complete a Task
4️⃣ Delete a Task
5️⃣ Exit
```

### 📌 Example Usage
```
Enter task name: "Finish project report"
✅ Task added: Finish project report

📋 Task List:
1. Finish project report - ❌

Enter task number to complete: 1
✅ Task 'Finish project report' marked as completed.

📋 Task List:
1. Finish project report - ✔️
```
### 🎯 Future Improvements
- ✅ Add due dates to tasks
- ✅ Implement categories for tasks
- ✅ Create a GUI version

### 🤝 Contributing
Pull requests are welcome!

### 📜 License
MIT License.
