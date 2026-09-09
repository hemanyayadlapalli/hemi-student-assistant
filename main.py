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

    while True:
        task = input("Enter a study task (or type 'done' to finish): ")

        if task.lower() == "done":
            break

        tasks.append(task)

  print("\nYour tasks:")

completed = []

for number, task in enumerate(tasks, start=1):
    completed.append(False)
    print(number, "-", task)

task_number = input("\nEnter the number of a completed task (or press Enter to skip): ")

if task_number:
    task_number = int(task_number)

    if 1 <= task_number <= len(tasks):
        completed[task_number - 1] = True

print("\nUpdated tasks:")

for number, task in enumerate(tasks, start=1):
    if completed[number - 1]:
        print(number, "-", task, "[Completed]")
    else:
        print(number, "-", task)

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
