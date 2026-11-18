"""Tests for adding tasks (feature/addtask)."""

import unittest

from task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager(storage_file=None)

    def test_add_task(self):
        """Adding a task stores it with id 1 and not completed."""
        task = self.manager.add_task("CSC418 Assignment 4", "Git and GitHub")
        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "CSC418 Assignment 4")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        """Empty and whitespace-only titles are rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
