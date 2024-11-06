# Task 1
# to do list


# this is an python module use to save the multiple tasks 
import json
class ToDoApp:
    def __init__(self,filename="tasks.json"):
        self.filename=filename
        self.tasks = self.load_tasks()
    def load_tasks(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            return[]
    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)
    def add_task(self, tasksInfo):
        self.tasks.append({"task information": tasksInfo, "completed": False})
        self.save_tasks()
        print("Task added!")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show!")
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['task information']} - {status}")
    def update_task(self, tasks_index):
            if (0 <= tasks_index < len(self.tasks)):
                self.tasks[tasks_index]["completed"] = not self.tasks[tasks_index]["completed"]
                self.save_tasks()
                print("Task updated!")
    def delete_task(self, task_index):
                if (0 <= task_index < len(self.tasks)):
                    del self.tasks[task_index]
                    self.save_tasks()
                    print("Task deleted!")
if __name__ == "__main__":
    app = ToDoApp()  # Create an instance of the app

    while True:
        # Show number of tasks as options
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ")

        # do tasks based on information given by the user
        if choice == "1":
            info = input("Enter task information: ")
            app.add_task(info)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            i = int(input("Enter task number to mark as done/undone: ")) - 1
            app.update_task(i)
        elif choice == "4":
            i = int(input("Enter task number to delete: ")) - 1
            app.delete_task(i)
        elif choice == "5":
            print("Exiting app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
