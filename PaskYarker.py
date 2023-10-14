def main():
    taskGroup = []
    def createTask():
        task = []
        task.append(input("Enter a name for a task: "))
        task.append(input("Enter a description for a task: "))
        task.append(input("Enter a due date for a task: "))
        task.append(input("Enter a priority for a task: "))
        task.append(False)
        taskGroup.append(task)
        print()

    def showTasks():
        i = 0
        while i < len(taskGroup):
            print(f"\nName: {taskGroup[i][0]}")
            print(f"Description: {taskGroup[i][1]}")
            print(f"Due date: {taskGroup[i][2]}")
            print(f"Priority: {taskGroup[i][3]}")
            if taskGroup[i][4] == True:
                print("Completed\n")
            else:
                print("Not completed\n")
            i += 1

    def showOneTask(index):
        print(f"\nName: {taskGroup[index][0]}")
        print(f"Description: {taskGroup[index][1]}")
        print(f"Due date: {taskGroup[index][2]}")
        print(f"Priority: {taskGroup[index][3]}")
        if taskGroup[index][4] == True:
            print("Completed\n")
        else:
            print("Not completed\n")        

    def findTask(text):
        string = input(text)
        x = 0
        while x < len(taskGroup):
            if taskGroup[x][0] == string:
                return x
            x += 1
        return -1
    
    def editTask(index):
        if index == -1:
            print("Task not found\n") 
            return
        string = input("What do you want to edit(name/description/due date/priority)\n")
        if string == "name":
            new_str = input(f"Choose a new name (currently it is '{taskGroup[index][0]}')\n")
            taskGroup[index][0] = new_str
            print(f"'{taskGroup[index][0]}' is now a new name for this task\n")

        if string == "description":
            new_str = input(f"Choose a new description (currently it is '{taskGroup[index][1]}')\n")
            taskGroup[index][1] = new_str
            print(f"'{taskGroup[index][1]}' is now a new description for this task\n")

        if string == "due date":
            new_str = input(f"Choose a new due date (currently it is '{taskGroup[index][2]}')\n")
            taskGroup[index][2] = new_str
            print(f"'{taskGroup[index][2]}' is now a new due date for this task\n")

        if string == "priority":
            new_str = input(f"Choose a new priority (currently it is '{taskGroup[index][3]}')\n")
            taskGroup[index][3] = new_str
            print(f"'{taskGroup[index][3]}' is now a new priority for this task\n")

    def deleteTask(index):
        if index == -1:
            print("task not found")
            return
        del taskGroup[index]
        print(f"Task '{taskGroup[index]}' has been deleted successfully\n")

    def markTask(index):
        if "y" in input("Do yo want mark it as complete?[y/n]\n").lower():
            taskGroup[index][4] = True
            print(f"Task '{taskGroup[index][0]}' has been marked as complete\n")
        else:
            print(f"Task '{taskGroup[index][0]}' has been marked as not complete\n")
            taskGroup[index][4] = False

    while True:

        print("Welcome to Pask Yraker")
        print("Enter 'info' for more info about this app")
        print("Enter 'list' to show a list of all tasks")
        print("Enter 'show' to show a specific task")
        print("Enter 'create' to create a new task")
        print("Enter 'edit' to edit any task")
        print("Enter 'delete' to delete any task")
        print("Enter 'mark' to mark any task as completed or not completed")
        uIn = input().strip().lower()
        print()

        if uIn == 'info':
            print("Pask Yarker is a simple console task traker app made with python")
            print("In Pask Yarker you can store tasks you need to do, their description, due date, priority and if it is finished")
            print("This app was made by BotWithDot\n")

        elif uIn == 'create':
            createTask()

        elif taskGroup == []:
            print("You have to create at least one task\n")

        elif uIn == 'list':
            showTasks()
            print("optinally choose to sort by date or by priority(TBA)\n")

        elif uIn == 'show':
            showOneTask(findTask("What task would you like to be shown\n"))

        elif uIn == 'edit':
            editTask(findTask("Choose a task you want to edit\n"))

        elif uIn == 'delete':
            deleteTask(findTask("Choose a task you want to delete\n"))

        elif uIn == 'mark':
            markTask(findTask("Choose a task to mark as complete or not complete\n"))

main()
