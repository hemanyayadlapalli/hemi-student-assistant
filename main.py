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

    task = input("Enter a study task: ")
    tasks.append(task)

    print("\nYour tasks:")
    for task in tasks:
        print("-", task)

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
