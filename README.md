# Student Task Manager

A small Python console application to add, display, complete, and delete
student tasks. Built for CSC418 — DevOps for Cloud Computing, Lab Assignment 4
(COMSATS University Islamabad, Lahore Campus, Fall 2026).

Project status: In Progress — v1.0.0 release in preparation

- **Author:** Muhammad Muneeb Azhar (SP23-BSE-125)
- **Course:** CSC418 DevOps for Cloud Computing — Dr. M. Hasanain Chaudary
- **Repository:** https://github.com/monebzz/studenttaskmanager
- **Release:** v1.0.0 — https://github.com/monebzz/studenttaskmanager/releases/tag/v1.0.0

## Features

- **Add a task** — title plus an optional description. Empty or
  whitespace-only titles are rejected (`feature/addtask`).
- **Display tasks** — every task listed with its number, title and
  status: `[ ]` for pending, `[x]` for completed.
- **Complete a task** — mark a selected task as completed by its
  task ID (`feature/completetask`).
- **Delete a task** — delete a task using a valid task ID; an
  unknown ID deletes nothing and shows an error
  (`feature/deletetask`).
- **Saved between runs** — tasks are stored in `tasks.json`
  (ignored by Git, see `.gitignore`).

## Setup

Requires Python 3.10 or newer. No extra packages are needed.

```bash
git clone https://github.com/monebzz/studenttaskmanager.git
cd studenttaskmanager
python3 main.py
```

## Usage

Run `python3 main.py` and follow the menu:

```text
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Example session:

```text
Choose an option (1-5): 1
Task title: CSC418 Assignment 4
Description (optional): Finish Git branching
Added task 1: CSC418 Assignment 4

Choose an option (1-5): 2
1. [ ] CSC418 Assignment 4 — Finish Git branching

Choose an option (1-5): 3
Task number to complete: 1
Completed task 1: CSC418 Assignment 4
```

A short user guide is in [`docs/userguide.md`](docs/userguide.md).

## Tests

Eight automated tests written with Python `unittest`:

```bash
python3 -m unittest discover -s tests -v
```

They cover adding a task, rejecting empty titles, completing a task
(including an unknown ID), deleting a task (including an unknown ID),
and displaying tasks. A GitHub Actions workflow
(`.github/workflows/tests.yml`) runs the same command on every push
to `main` and on every pull request to `main`.

## Project layout

```text
studenttaskmanager/
├── main.py                  # console menu
├── task_manager.py          # TaskManager: add / list / complete / delete
├── tests/                   # unittest tests (test_add_task, test_complete_task,
│                            #   test_delete_task, test_display)
├── .github/workflows/
│   └── tests.yml            # GitHub Actions: run tests on push / PR to main
├── docs/userguide.md        # short user guide
├── LABREPORT.md             # assignment report (Parts A–G)
├── labevidence/             # screenshots of key steps
├── README.md
├── LICENSE                  # MIT
└── .gitignore               # Python .gitignore
```

## Workflow used

Work was done on feature branches (`feature/addtask`,
`feature/completetask`, `feature/deletetask`, `feature/tests-actions`),
reviewed in pull requests linked to GitHub Issues, and merged into
`main`. One merge conflict in `README.md` was created on purpose
(two branches changing the same “Project status” line) and resolved
on `main` — see `LABREPORT.md` and `labevidence/`.
