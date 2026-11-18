"""Student Task Manager — console application.

Run:  python3 main.py
Menu: add / display / complete / delete / exit.
Tasks are saved to tasks.json on every change.
"""

from task_manager import TaskManager


def _read_id(prompt):
    """Read a task id from the user; return None on bad input."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Please enter a valid task number (e.g. 1).")
        return None


def main():
    manager = TaskManager()
    print("Student Task Manager")
    print("====================")
    while True:
        print("\n1. Add task")
        print("2. Display tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ")
            description = input("Description (optional): ")
            try:
                task = manager.add_task(title, description)
                manager.save()
                print(f"Added task {task['id']}: {task['title']}")
            except ValueError as e:
                print(f"Could not add task: {e}")
        elif choice == "2":
            print("\n" + manager.display_tasks())
        elif choice == "3":
            task_id = _read_id("Task number to complete: ")
            if task_id is None:
                continue
            try:
                task = manager.complete_task(task_id)
                manager.save()
                print(f"Completed task {task['id']}: {task['title']}")
            except ValueError as e:
                print(f"Could not complete task: {e}")
        elif choice == "4":
            task_id = _read_id("Task number to delete: ")
            if task_id is None:
                continue
            try:
                task = manager.delete_task(task_id)
                manager.save()
                print(f"Deleted task {task['id']}: {task['title']}")
            except ValueError as e:
                print(f"Could not delete task: {e}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
