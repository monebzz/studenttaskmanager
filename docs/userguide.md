# Student Task Manager — User Guide

## What it does

Student Task Manager is a small console app for keeping track of
study tasks. You can add a task, see all your tasks, mark one as
done, and delete one you no longer need. Tasks are saved in a file
called `tasks.json` in the same folder, so they are still there the
next time you run the app.

## Starting the app

You need Python 3.10 or newer, and nothing else to install.

```bash
git clone https://github.com/monebzz/studenttaskmanager.git
cd studenttaskmanager
python3 main.py
```

You will see this menu:

```text
Student Task Manager
====================

1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of what you want to do and press Enter.

## Adding a task

Choose **1**. Type a title and press Enter, then type a short
description (or just press Enter to skip it).

```text
Task title: CSC418 Assignment 4
Description (optional): Finish Git branching
Added task 1: CSC418 Assignment 4
```

A title cannot be empty. If you press Enter without typing
anything, or type only spaces, the app tells you the title cannot
be empty and nothing is added.

## Displaying tasks

Choose **2**. Every task is shown on one line with its number,
a status box, and its title:

```text
1. [ ] CSC418 Assignment 4 — Finish Git branching
2. [x] Revise for viva
```

`[ ]` means the task is still pending. `[x]` means it is completed.
If you have no tasks yet, the app says so.

## Completing a task

Choose **3** and type the task number shown in the list.

```text
Task number to complete: 1
Completed task 1: CSC418 Assignment 4
```

If you type a number that does not belong to any task, the app
says there is no task with that ID and nothing changes.

## Deleting a task

Choose **4** and type the task number.

```text
Task number to delete: 1
Deleted task 1: CSC418 Assignment 4
```

Only that one task is deleted. The other tasks keep their numbers
and their order. As with completing, an unknown number shows an
error and deletes nothing.

## Leaving the app

Choose **5**. Your tasks are already saved, so you can come back
later with `python3 main.py` and they will still be there.

## If something goes wrong

- **“Task title cannot be empty.”** — type a real title.
- **“No task with id …”** — choose 2 first and use a number from
  the list.
- **“Please enter a valid task number”** — type a whole number,
  for example `1`, not a word.
- **Tasks are gone after a fresh clone** — that is expected.
  `tasks.json` is your own local file and is not stored in Git.
