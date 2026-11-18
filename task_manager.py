"""Student Task Manager — core logic.

A task is a small dict: {"id": int, "title": str,
"description": str, "completed": bool}.

TaskManager keeps tasks in memory and can save / load them from a
JSON file (tasks.json) so tasks survive between runs. The console
menu in main.py is only a thin layer over this class, which is what
the unit tests in tests/ exercise.
"""

import json
import os


class TaskManager:
    """Manage a list of student tasks."""

    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = []
        self._next_id = 1
        if storage_file and os.path.exists(storage_file):
            self.load()

    # -- helpers -------------------------------------------------
    def _find(self, task_id):
        """Return the task with this id, or None."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    # -- core operations -----------------------------------------
    def add_task(self, title, description=""):
        """Add a task. Empty titles are rejected (see feature/addtask)."""
        if title is None or not str(title).strip():
            raise ValueError("Task title cannot be empty.")
        task = {
            "id": self._next_id,
            "title": str(title).strip(),
            "description": str(description or "").strip(),
            "completed": False,
        }
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        """Return all tasks in the order they were added."""
        return list(self.tasks)

    def display_tasks(self):
        """Return a printable listing, one line per task."""
        if not self.tasks:
            return "No tasks yet. Add one from the menu."
        lines = []
        for task in self.tasks:
            status = "[x]" if task["completed"] else "[ ]"
            line = f"{task['id']}. {status} {task['title']}"
            if task["description"]:
                line += f" — {task['description']}"
            lines.append(line)
        return "\n".join(lines)

    def complete_task(self, task_id):
        """Mark the task with this id as completed."""
        task = self._find(task_id)
        if task is None:
            raise ValueError(f"No task with id {task_id}.")
        task["completed"] = True
        return task

    def delete_task(self, task_id):
        """Delete the task with this id and return it."""
        task = self._find(task_id)
        if task is None:
            raise ValueError(f"No task with id {task_id}.")
        self.tasks.remove(task)
        return task

    # -- persistence ----------------------------------------------
    def save(self):
        if not self.storage_file:
            return
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(
                {"next_id": self._next_id, "tasks": self.tasks},
                f, indent=2,
            )

    def load(self):
        with open(self.storage_file, encoding="utf-8") as f:
            data = json.load(f)
        self.tasks = data.get("tasks", [])
        self._next_id = data.get(
            "next_id",
            max((t["id"] for t in self.tasks), default=0) + 1,
        )
