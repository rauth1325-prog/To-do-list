import json

# ---------------- LOAD MEMORY ----------------

try:
    with open("data.json", "r") as file:
        data = json.load(file)

    Tasks = data["Tasks"]
    Bithday = data["Bithday"]
    Fesiival = data["Fesiival"]

except FileNotFoundError:
    Tasks = []
    Bithday = []
    Fesiival = []


# ---------------- SAVE MEMORY ----------------

def save_data():
    data = {
        "Tasks": Tasks,
        "Bithday": Bithday,
        "Fesiival": Fesiival
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# ---------------- TASKS ----------------

while True:

    a = input("Add tasks / See tasks / Delete tasks / Exit: ")

    if a.lower() == "add tasks":

        task = input("Enter the task you want to add: ")
        Tasks.append(task)

        save_data()
        print("Task saved!")

    elif a.lower() == "see tasks":

        print("Your tasks are:", Tasks)

    elif a.lower() == "delete tasks":

        task = input("Enter the task you want to delete: ")

        if task in Tasks:
            Tasks.remove(task)
            save_data()
            print("Task deleted!")

        else:
            print("Task is not present.")

    elif a.lower() == "exit":

        print("Goodbye!")
        break


# ---------------- BIRTHDAYS ----------------

while True:

    a = input("Do you want to save anyone's Birthday date? ")

    if a.lower() == "yes":

        name = input("Write the name of person: ")
        date = input("Write the Birth date of person: ")

        Bithday.append([name, date])
        save_data()

    else:
        print("Okay, thanks for visiting us :)")
        break


# ---------------- FESTIVALS ----------------

while True:

    a = input("Any festival you want to remember? ")

    if a.lower() == "yes":

        name = input("Name of festival: ")
        date = input("Date of festival: ")

        Fesiival.append([name, date])
        save_data()

    else:
        print("Thanks for visiting")
        break


print("Stay Happy!!!")