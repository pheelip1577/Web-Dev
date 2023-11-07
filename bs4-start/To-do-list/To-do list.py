
# Your existing functions (add_task, complete_task, remove_task, etc.)

@app.route('/', methods=['GET', 'POST'])


import pickle
print("*******WELCOME TO YOUR TO-DO LIST*******")



tasks = []

if __name__ == "__main__":

    def add_tasks():
        task_name = input("Add a task: ")
        priority = input("How important is this task (high,medium or low): ")
        tasks.append({"Name": task_name, "priority": priority, "task_status": False} )
        print("Task has been added succesfully")

    def view_tasks():
        for index, task in  enumerate(tasks, start = 1):
            status = "Completed" if task["task_status"] else "Not Completed "
            print(f"{index}. {task['Name']} - Priority: {task.get('priority')} - Status: {status}")

    def complete_task():
        view_tasks()
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_number]["task_status"] = True
        print("Task marked as completed!")

    def remove_task():
        view_tasks()
        task_number = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task['Name']}' has been removed!")

    def save_tasks():
        with open("tasks.pickle", "wb") as f:
            pickle.dump(tasks, f)

    def load_tasks():
        try:
            with open("tasks.pickle", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []


    def sort_tasks():
        tasks.sort(key=lambda task: (task.get["task_status"], task["Name"]))

    def main():
        global tasks
        tasks = load_tasks()
        
        while True:
            print("\n===== TO-DO LIST =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Remove Task")
            print("5. Save and Exit")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                add_tasks()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                complete_task()
            elif choice == "4":
                remove_task()
            elif choice == "5":
                save_tasks()
                print("Tasks saved. Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


    main()



