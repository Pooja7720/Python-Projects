# from fastapi import FastAPI

# app = FastAPI()

def addTask(to_do_list):
    element = input("\nEnter the task to add in To Do List:")
    to_do_list.append(element)

def display_todo(to_do_list):
    print("***** TO DO LIST *****")
    for task in to_do_list:
        print(f"{to_do_list.index(task)+1}. {task}")

def updateTask(to_do_list):
    srNo = int(input("\nEnter the serial number of task to update:"))
    indexVal = srNo - 1
    if indexVal > len(to_do_list)-1:
        # IF GIVEN SR NO IS NOT PRESENT IN TO DO LIST
        print("\nSorry! No such sr.no present in given To Do List...")
    else:
        # GIVEN SR NO IS PRESENT IN TO DO LIST
        oldTask = to_do_list[indexVal]
        newTask = input(f"\nEnter the task which you want to update at {oldTask}:")
        to_do_list[indexVal] = newTask
        print("\nYour task updated successfully")
        print("\nLoading updated To Do List...")
        display_todo(to_do_list)

def deleteTask(to_do_list):
    srNo = int(input("\nEnter the serial number of task to delete:"))
    indexVal = srNo - 1
    if indexVal > len(to_do_list)-1:
        # IF GIVEN SR NO IS NOT PRESENT IN TO DO LIST
        print("\nSorry! No such sr.no present in given To Do List...")
    else:
        to_do_list.remove(to_do_list[indexVal])
        print("\nYour task deleted successfully")
        print("\nLoading updated To Do List...")
        display_todo(to_do_list)

def clearTodo(to_do_list):
    print("\nClearing To Do List...")
    to_do_list.clear()
    print("\nAfter clearing To Do List")
    display_todo(to_do_list)

# @app.get("/")
# async def root():
# CREATE A TO DO LIST

to_do_list = []
userChoice = "yes"
task = 0

while userChoice == "yes":
    # TAKING CHOICE FROM USER TO MANIPULATE TO DO LIST
    task = int(input("\nEnter your choice:\n1.Create a todo list\n2.Add task\n3.Update task.\n4.Delete Task\n5.Display to do list\n6.Clear todo list\n7.Exit\n"))
    if task == 1:
        # CREATE A TODO LIST
        if len(to_do_list) == 0:
            # CREATING TO DO LIST FOR FIRST TIME
            print("\nCreating a to do list...")
            addTask(to_do_list)
        else:
            # YOUR TO DO LIST IS ALREADY CREATED, DISPLAYING IT
            print("\nYour todo list is already created...")
            display_todo(to_do_list)

    elif task ==2:
        # ADD TASK IN TO DO LIST
        addTask(to_do_list)

    elif task == 3:
        # UPDATING THE TASK
        updateTask(to_do_list)
    
    elif task == 4:
        # DELETING ELEMENT FROM TO DO LIST
        deleteTask(to_do_list)
    
    elif task == 5:
        # DISPLAY TO DO LIST
        display_todo(to_do_list)

    elif task == 6:
        # CLEARING TO DO LIST
        clearTodo(to_do_list)

    elif task ==7:
        # EXITING FROM THE APPLICATION
        userChoice = "No"
        
        
        
    