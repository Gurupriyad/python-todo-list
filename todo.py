import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def display_tasks(tasks):
    print("\n===== TO-DO LIST =====")

    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    print()


def main():
    tasks = load_tasks()

    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ").strip()

            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added successfully.\n")
            else:
                print("Task cannot be empty.\n")

        elif choice == "3":
            display_tasks(tasks)

            if tasks:
                try:
                    number = int(input("Enter task number to remove: "))

                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}\n")
                    else:
                        print("Invalid task number.\n")

                except ValueError:
                    print("Please enter a valid number.\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()