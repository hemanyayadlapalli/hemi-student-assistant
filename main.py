print("=" * 35)
print("      HEMI STUDENT ASSISTANT")
print("=" * 35)

user_name = input("Enter your name: ")

print("\nWelcome,", user_name + "!")
print("\nWhat would you like to do?")

print("1. Study Tasks")
print("2. Grade Calculator")
print("3. Study Timer")
print("4. Quiz")
print("5. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    print("\nStudy Tasks")

    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append([task, status])
    except FileNotFoundError:
        pass

    while True:
        task = input("Enter a study task (or type 'done' to finish): ")

        if task.lower() == "done":
            break

        tasks.append([task, "incomplete"])

    if tasks:
        print("\nYour tasks:")

        for number, task in enumerate(tasks, start=1):
            status = task[1]

            if status == "complete":
                print(number, "-", task[0], "[Completed]")
            else:
                print(number, "-", task[0])

        task_number = input(
            "\nEnter the number of a completed task (or press Enter to skip): "
        )

        if task_number:
            task_number = int(task_number)

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1][1] = "complete"

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task[0] + "|" + task[1] + "\n")

        print("\nUpdated tasks:")

        for number, task in enumerate(tasks, start=1):
            if task[1] == "complete":
                print(number, "-", task[0], "[Completed]")
            else:
                print(number, "-", task[0])

    else:
        print("\nNo tasks added yet.")

elif choice == "2":
    print("\nGrade Calculator")

elif choice == "3":
    print("\nStudy Timer")

elif choice == "4":
    print("\nQuiz")

elif choice == "5":
    print("\nGoodbye,", user_name + "!")

else:
    print("\nInvalid choice. Please select a number from 1 to 5.")
