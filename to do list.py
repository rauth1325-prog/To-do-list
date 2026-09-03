Tasks = []

while True:

    a = input("Add tasks / See tasks / Delete tasks / Exit: ")

    if a.lower() == "add tasks":

        task = input("Enter the task you want to add: ")
        Tasks.append(task)

    elif a.lower() == "see tasks":

        print("Your tasks are:", Tasks)

    elif a.lower() == "delete tasks":

        task = input("Enter the task you want to delete: ")

        if task in Tasks:
            Tasks.remove(task)
            print("Task deleted!")
        else:
            print("Task is not present.")

    elif a.lower() == "exit":

        print("Goodbye!")
        break
Bithday = []
while True:
    a = input("Do you want to save anyones Birthday date ")
    if a.lower() == "yes":
        name = input("Write the name of person")
        date = input("Write the Birth date of person")
        Bithday.append([name,date])
    else:
        print("ok thanks to visit us :) ")
        break
    
Fesiival = []
while True:
    a= input("any festival you want to remember")
    if a.lower() == "yes":
        name  = input("Name of festival")
        date = input("Date of festival")
        Fesiival.append([name,date])
    else:
        print("Thanks to visit ")
        break    

print("Stay Consistent!!!")