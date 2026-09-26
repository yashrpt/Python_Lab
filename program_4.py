
tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task")
    print("2. Execute Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        condition = input("Is the task ready? (yes/no): ").lower()

        if condition == "yes":
            tasks.append((task, True))
            print("Task added successfully.")
        elif condition == "no":
            tasks.append((task, False))
            print("Task added but not ready.")
        else:
            print("Invalid condition.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            task, ready = tasks[0]

            if ready and task:
                print("Executing task:", task)
                tasks.pop(0)
            elif not ready or not task:
                print("Task cannot be executed.")
            else:
                print("Invalid task.")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nScheduled Tasks:")
            for task, ready in tasks:
                print(task, "- Ready" if ready else "- Not Ready")

    elif choice == "4":
        print("Exiting Task Scheduler.")
        break

    else:
        print("Invalid choice. Try again.")