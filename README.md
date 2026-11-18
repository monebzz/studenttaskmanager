# Student Task Manager

A small Python console application to add, display, complete, and delete
student tasks. Built for CSC418 — DevOps for Cloud Computing, Lab Assignment 4.

Project status: In Progress — v1.0.0 release in preparation

## Features

- Add a task with a title and an optional description
- Display all tasks with their status
- Mark a selected task as completed
- Delete a task using its task ID

## Setup

```bash
git clone https://github.com/monebzz/studenttaskmanager.git
cd studenttaskmanager
python3 main.py
```

Requires Python 3.10 or newer. No extra packages are needed.

## Usage

Run `python3 main.py` and follow the menu:

1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit

## Tests

```bash
python3 -m unittest discover -s tests -v
```
