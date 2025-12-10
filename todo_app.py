tasks = []

while True:
    print("\n1. Add task")
    print("\n2. view task")
    print("\n3. delete task")
    print("\n4. Exit")


    choice = input("choose:")
    if choice == "1":
        task = input("enter task")
        tasks.append(task)
    elif choice == "2":
        for i,task in enumerate(tasks):
          print(f"{i}:{task}")
    elif choice == "3":
        num = int(input("enter the task to delete:"))
        tasks.pop(num-1)
    elif choice == "4":
        break          
