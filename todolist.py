class TodoList:
    def __init__(self):
        self.tasks=[]
    def display_tasks(self):
        if self.tasks:
            print("your Todo List")
            for id, task in enumerate(self.tasks,start=1):
                  print(f"{id}. {task}")
        else:
            print("your todolist is empty")
    def add_task(self,task):
        self.tasks.append(task)
        print("task added successfully..")
    def remove_task(self,task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")
    def update_task(self,task_index):
        value=input("Enter a updated task  :")
        self.tasks[task_index-1]=value
        print("updated task successfully")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '4':
            todo_list.display_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            todo_list.update_task(task_index)
        elif choice == '5':
            print("Thank you for using the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()