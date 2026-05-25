todo_list = []

while True:
    print("\n📌 To-Do List")
    print("1. ➕ Add task")
    print("2. 📄 View tasks")
    print("3. 🗑️ Remove task")
    print("4. 🚪 Exit")
    print("5. ✏️ Edit task")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("✅ Task added.")

    elif choice == '2':
        print("📄 Tasks:")
        i = 0
        while i < len(todo_list):
            print(str(i+1) + ". " + todo_list[i])
            i = i + 1

    elif choice == '3':
        print("🗑️ Tasks:")
        i = 0
        while i < len(todo_list):
            print(str(i+1) + ". " + todo_list[i])
            i = i + 1
        num = input("Enter the number of the task to remove: ")
        num = int(num)
        if num > 0 and num <= len(todo_list):
            todo_list.pop(num-1)
            print("🗑️ Task removed.")
        else:
            print("⚠️ Invalid number.")

    elif choice == '4':
        print("👋 Goodbye!")
        break

    elif choice == '5':
        print("✏️ Tasks:")
        i = 0
        while i < len(todo_list):
            print(str(i+1) + ". " + todo_list[i])
            i = i + 1
        num = input("Enter the number of the task to edit: ")
        num = int(num)
        if num > 0 and num <= len(todo_list):
            new_task = input("Enter the new task text: ")
            todo_list[num-1] = new_task
            print("✏️ Task updated.")
        else:
            print("⚠️ Invalid number.")

    else:
        print("⚠️ Please enter a valid option.")